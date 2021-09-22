#!/usr/bin/env python

import requests
import json
import sys


# the variables below assume the user is leveraging the
# always on sandbox.
HOST = 'sandbox-iosxe-latest-1.cisco.com'
# use the NETCONF port for your IOS-XE device
PORT = 443
# use the user credentials for your IOS-XE device
USER = 'developer'
PASS = 'C1sco12345'


def main():
    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    }

    response = requests.get(url, headers=headers, verify=False, auth=(USER, PASS)).json()
    print(json.dumps(response, indent=2))

    interface_list = response["ietf-interfaces:interfaces"]["interface"]
    for interface in interface_list:
        print(interface["name"])


if __name__ == '__main__':
    sys.exit(main())

