#!/usr/bin/env python

import requests
import json
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
    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }
    payload = json.dumps({
        "ietf-interfaces:interface": {
            "name": "Loopback800",
            "description": "Added using RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": "88.88.88.80",
                    "netmask": "255.255.255.255"
                    }
                ]
            }
        }
    })

    response = requests.post(url, headers=headers, data=payload, auth=(USER,PASS), verify=False)
    if response.ok:
        print(response.status_code)
        print("Loopback created. Use the get_loopback or get_interfaces_config module to verify.")


if __name__ == '__main__':
    sys.exit(main())
