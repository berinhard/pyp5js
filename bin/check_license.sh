#!/bin/bash

EXIT_CODE=0

while IFS= read -r -d '' file; do
    if ! head -5 "$file" | grep -q 'Copyright'; then
      echo "$file" is missing a license
      EXIT_CODE=1
    fi
done < <(find pyp5js -type f \( \
            -name "*.py" -o \
            -name "*.html" -o \
            -name "*.js.template" \) -print0)

exit $EXIT_CODE
