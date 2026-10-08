#!/usr/bin/env bash
# leak-check.sh — verhindert, dass Secrets, grosse Dateien oder Begriffe aus einer
# Sperrliste ins Repo gelangen.
#
#   scripts/leak-check.sh          prüft die gestageten Dateien (Pre-Commit-Modus)
#   scripts/leak-check.sh --all    prüft alle Dateien im Arbeitsverzeichnis
#
# Sperrliste: eine Textdatei ausserhalb des Repos, ein Begriff je Zeile, Zeilen mit #
# sind Kommentare. Pfad per Umgebungsvariable LEAK_SPERRLISTE oder in der Datei
# .git/leak-sperrliste-pfad (eine Zeile). Ohne Sperrliste laufen nur die generischen
# Prüfungen. Die Sperrliste gehört NICHT ins Repo.
#
# Installation als Hook:  cp scripts/leak-check.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit

set -u
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

MODE="${1:-staged}"
MAX_BYTES=$((1024 * 1024))
FAIL=0

# --- Dateiliste ---------------------------------------------------------------
if [ "$MODE" = "--all" ]; then
  FILES=$(git ls-files --cached --others --exclude-standard 2>/dev/null || find . -type f -not -path './.git/*')
else
  FILES=$(git diff --cached --name-only --diff-filter=ACMR 2>/dev/null)
fi
[ -z "$FILES" ] && { echo "leak-check: keine Dateien zu prüfen."; exit 0; }

# --- Sperrliste finden --------------------------------------------------------
LIST="${LEAK_SPERRLISTE:-}"
if [ -z "$LIST" ] && [ -f .git/leak-sperrliste-pfad ]; then
  LIST=$(head -1 .git/leak-sperrliste-pfad)
fi
if [ -n "$LIST" ] && [ -f "$LIST" ]; then
  TERMS=$(grep -v '^\s*#' "$LIST" | grep -v '^\s*$')
else
  TERMS=""
  echo "leak-check: keine Sperrliste gefunden, nur generische Prüfungen."
fi

# --- Generische Muster (Tokens, Keys) -----------------------------------------
TOKEN_RE='(EAA[A-Za-z0-9]{30,}|shpat_[A-Za-z0-9]{20,}|shpss_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|xox[abp]-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30,}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----)'

while IFS= read -r f; do
  [ -f "$f" ] || continue

  # 1. .env-Dateien
  case "$(basename "$f")" in
    .env|.env.*)
      if [ "$(basename "$f")" != ".env.example" ]; then
        echo "BLOCK  $f  (.env-Datei)"; FAIL=1
      fi;;
  esac

  # 2. Grösse
  size=$(wc -c < "$f" | tr -d ' ')
  if [ "$size" -gt "$MAX_BYTES" ]; then
    echo "BLOCK  $f  ($((size / 1024)) KB > 1 MB)"; FAIL=1
  fi

  # Binärdateien nicht nach Text durchsuchen
  if ! grep -Iq . "$f" 2>/dev/null; then continue; fi

  # 3. Token-Muster
  if grep -nE "$TOKEN_RE" "$f" >/dev/null 2>&1; then
    grep -nE "$TOKEN_RE" "$f" | sed -E 's/(.{0,80}).*/\1/' | while IFS= read -r line; do
      echo "BLOCK  $f:$line  (Token-Muster)"
    done
    FAIL=1
  fi

  # 4. Sperrliste
  if [ -n "$TERMS" ]; then
    while IFS= read -r term; do
      [ -z "$term" ] && continue
      if grep -niF -- "$term" "$f" >/dev/null 2>&1; then
        grep -niF -- "$term" "$f" | head -3 | sed -E 's/(.{0,100}).*/\1/' | while IFS= read -r line; do
          echo "BLOCK  $f:$line  (Sperrliste: $term)"
        done
        FAIL=1
      fi
    done <<< "$TERMS"
  fi
done <<< "$FILES"

if [ "$FAIL" -ne 0 ]; then
  echo
  echo "leak-check: ABGEBROCHEN. Treffer oben beheben, dann erneut committen."
  exit 1
fi
echo "leak-check: sauber ($(echo "$FILES" | wc -l | tr -d ' ') Dateien)."
exit 0
