## Ping by hands
ansible all -m ping -i inventory.yaml
//* ansible subject -m ping -i inventory.yaml

## Check with playbook
ansible-playbook -i inventory.yaml playbook.yaml

## Check for apps
ansible-playbook -i inventory.yaml playbook-01.yaml -u gidra -K