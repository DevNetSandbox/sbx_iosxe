#!/usr/bin/env python

import requests
import sys


# the variables below assume the user is leveraging the
# always on sandbox.
HOST = 'sandbox-iosxe-latest-1.cisco.com'
# use the RESTCONF port for your IOS-XE device
PORT = 443
# use the user credentials for your IOS-XE device
USER = 'developer'
PASS = 'C1sco12345'


def main():
    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces/interface=Loopback800"
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }

    response = requests.delete(url, headers=headers, auth=(USER,PASS), verify=False)
    if response.ok:
        print(response.status_code)
        print("Loopback deleted. Use the get_loopback or get_interfaces_config module to verify.")


if __name__ == '__main__':
    sys.exit(main())
