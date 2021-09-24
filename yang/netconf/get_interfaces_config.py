#!/usr/bin/env python
#
# Get configured interfaces using Netconf
#
# darien@sdnessentials.com
#

from ncclient import manager
import sys
import xml.dom.minidom


# the variables below assume the user is leveraging the
# always on sandbox.
HOST = 'sandbox-iosxe-latest-1.cisco.com'
# use the NETCONF port for your IOS-XE device
PORT = 830
# use the user credentials for your IOS-XE device
USER = 'developer'
PASS = 'C1sco12345'

# XML file to open
FILE = 'get_interfaces.xml'


# create a main() method
def get_configured_interfaces(xml_filter):
    """
    Main method that retrieves the interfaces from config via NETCONF.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
        with open(xml_filter) as f:
            return(m.get_config('running', f.read()))


def main():
    """
    Simple main method calling our function.
    """
    interfaces = get_configured_interfaces(FILE)
    print(xml.dom.minidom.parseString(interfaces.xml).toprettyxml())

if __name__ == '__main__':
    sys.exit(main())
