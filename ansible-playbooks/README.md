# IOS XE Sandbox Sample Ansible Playbooks

So you are interested in leveraging Ansible for configuration management of your IOS XE devices and are kicking the tires using the [IOS XE Programmability Sandbox]().  Well, you are in the right place!  

Here you will find some sample playbooks to deploy common configurations and topologies that are all ready to run against the Sandbox.  Just clone down the repository and jump right in.  

### Quick Links

* [Code and Ansible Setup](#code-and-ansible-setup)
* [Sample Topologies and Configs](#sample-topologies-and-configs)

# Code and Ansible Setup

Before you can run your first playbook, you need to:

2. Download/clone the sample code repository
3. Setup your workstation for Ansible.  

## Get the Sample Code

The simplest way to get the code is to just `git clone` it to your local machine.  

```bash
# from the directory where you want to put the code
git clone https://github.com/DevNetSandbox/sbx_iosxe
cd sbx_iosxe
```

If you'd like to get your very own copy of the repository that you can update or add code to, you may want to "Fork" the repo and clone down your own copy.  And please submit Pull Requests for anything cool you build in the Sandbox!  

### Download with out git

If you'd rather just download the code without mucking around with `git`, you can do that too.  Just hit this link to download a zip file with the code:  [DevNetSandbox/sbx_iosxe/archive/master.zip](https://github.com/DevNetSandbox/sbx_iosxe/archive/master.zip)

## Setup Ansible

Ansible is written in Python which means you set it up using the same steps as any Python application.  Like other Python projects, we highly recommend leveraging [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/) with Ansible for the best experience.  

Follow these example steps to create a virtual environment and install the requirements.  

```bash
python3.6 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Now Ansible is installed and ready to go.  One last step before running any of the sample playbooks is to tell Ansible about the target hosts in the sandbox, and the credentials to use to access.  

For the hosts part, included in the directory is `.ansible.cfg` (see it [here](.ansible.cfg)).  This is a standard Ansible file that identifies the default location of the inventory.  By including the file within the directory, Ansible will use the [hosts](hosts) file located within the repo.  

This `hosts` file contains details on the different IOS XE Always on and Reservable Sandboxes from DevNet.  The playbooks are configured to execute against the Always-On Sandboxes, but you can update the sample playbooks to target a reservable sandbox if you have one.  
