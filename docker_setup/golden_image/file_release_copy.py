#!/usr/env/bin python3
from pathlib import Path
import hashlib
import shutil

if Path('../../vim_setup/.vimrc').exists():
    print("Ready for copy: 'vim_setup/.vimrc'")
else:
    print("No source 'vim_setup/.vimrc'")

source_path = Path('../../vim_setup/.vimrc')
python_path = Path('./python_way/.vimrc')
nodejs_path = Path('./nodejs_way/.vimrc')

with open(source_path, 'rb') as source_heap:
    source_content = source_heap.read()
    source_hash = hashlib.md5(source_content).hexdigest()
    source_heap.close()

with open(python_path, 'rb') as python_heap:
    python_content = python_heap.read()
    python_hash = hashlib.md5(python_content).hexdigest()
    python_heap.close()

with open(nodejs_path, 'rb') as nodejs_heap:
    nodejs_content = nodejs_heap.read()
    nodejs_hash = hashlib.md5(nodejs_content).hexdigest()
    nodejs_heap.close()

print ("source checksum:", source_hash[0:4] + ", ", "python checksum:", python_hash[0:4] + ", ", "nodejs checksum:", nodejs_hash[0:4])

if source_hash == python_hash and source_hash == nodejs_hash:
    print("* No update needed *")
else:
    print("* Let's start update *")

if source_hash != python_hash:
    shutil.copy2('../../vim_setup/.vimrc', './python_way/')
    print("python way updated")

if source_hash != nodejs_hash:
    shutil.copy2('../../vim_setup/.vimrc', './nodejs_way/')
    print("nodejs way updated")
