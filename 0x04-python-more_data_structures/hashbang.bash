#!/usr/bin/bash
for file in *.py; do echo '#!/usr/bin/python3' > "$file"; done
# for file in *.py; do echo '#!/usr/bin/python3' | cat - "$file" > temp && mv temp "$file"; done