##This is a very simple demo for how to use ansible to mange CISCO IOS-XE device inluding C9000 Serial Swith.

##Env Description:

This virtualenv has included python3 enviroment with ansible(2.7.5).
Just use the linux shell cmd "#source ansible-playbooks-py3/bin/activate" to active the virtualenv.

##ansible Detail:

1.Move the 'ansible.cfg' to /etc/ansible/hosts , modify the IP address, User name ,Password and ssh port.
2.use the the linux shell cmd "#ansible-playbook ansible.yml" to run the command you want to excute on the device in "/etc/ansible/hosts".
3. If your device has enable authentication, please use the 'ansible_with_enable_mode.yml',and with " --extra-vars='ansible_become_pass=password''" afther the ansible-playbook command.
4. If you want to see the excuete result , please use -vvv afther the whole "ansible-palybook" command.
