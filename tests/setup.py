from testinfra.utils.ansible_runner import AnsibleRunner as runner

inventory = runner('.molecule/ansible_inventory')
