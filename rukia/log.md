# rukia -- automation of node.js deployment

## ask sudo password

ansible-playbook ./playbooks/app-playbook.yaml -i ./inventories/staging/inventory.yaml --ask-become-pass

### Node Version Manager

<https://github.com/nvm-sh/nvm>

## nvm, npm and node

after ~/.nvm/install.sh

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

nvm --version
npm --version
node --version
