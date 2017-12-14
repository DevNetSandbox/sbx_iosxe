#!/usr/bin/env python

from ncclient import manager
import sys


# the variables below assume the user is leveraging the
# network programmability lab and accessing csr1000v
# use the IP address or hostname of your CSR1000V device
HOST = '10.10.20.48'
# use the NETCONF port for your IOS-XE device
PORT = 830
# use the user credentials for your IOS-XE device
USER = 'cisco'
PASS = 'cisco_1234!'



# create a main() method
def main():
    """
    Main method that prints netconf capabilities of remote device.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:

        # print all NETCONF capabilities
        print('***Here are the Remote Devices Capabilities***')
        for capability in m.server_capabilities:
            print(capability.split('?')[0])

if __name__ == '__main__':
    sys.exit(main())
