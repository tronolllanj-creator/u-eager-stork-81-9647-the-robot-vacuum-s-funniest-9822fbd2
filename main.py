import os
from pathlib import Path

EXCUSE = "I mistook the corner for a cliff. Fear is a valid cleaning strategy, legally speaking."

# Line: I mistook the corner for a cliff. Fear is a valid cleaning strategy, legally speaking.
# Exact character count: 86 (within 1-120)

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
path = Path(output_dir) / 'entry.txt'

path.write_text(EXCUSE, encoding='utf-8')
