## rukia -- automation of node.js deployment


### ask sudo password
ansible-playbook ./playbooks/app-playbook.yaml -i ./inventories/staging/inventory.yaml --ask-become-pass
