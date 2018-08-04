#!/usr/bin/env python3

import json

t = json.load(open('translations.json'))

out = open('lean.mim', 'w')

out.write(r'''
;; lean.mim -- Input method using abbreviations from the Lean proof assistant

;; Converted from https://github.com/leanprover/vscode-lean/translations.json

(input-method t lean)

(description "Input method using abbreviations from the Lean proof assistant

Example: \\nat \\to \\com
")

(title "Lean")

(map (map
''')

for k, v in sorted(t.items(), key = lambda i: i[0]):
    k = '\\' + k
    k = k.replace('\\', '\\\\')
    k = k.replace('"', '\\"')
    out.write('  ("{0}" "{1}")\n'.format(k, v))

out.write(r'''
))

(state (init (map)))
''')