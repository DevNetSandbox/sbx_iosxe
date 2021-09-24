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
    url = f"https://{HOST}:{PORT}/restconf/data/netconf-state/capabilities"
    headers = {
      'Content-Type': 'application/yang-data+json',
      'Accept': 'application/yang-data+json',
    }

    response = requests.get(url, headers=headers, verify=False, auth=(USER, PASS)).json()
    print(json.dumps(response, indent=2))


if __name__ == '__main__':
    sys.exit(main())
