from pyats import aetest
import logging

# Needed for aetest script
from ats import aetest
from ats.log.utils import banner


# Genie Imports
from genie.conf import Genie
from genie.abstract import Lookup

# import the genie libs
from genie.libs import ops  # noqa

# import API libriries
from ncclient import manager
import requests
import xmltodict

# Get your logger for your script
log = logging.getLogger(__name__)


MAX_RETRIES = 2


###################################################################
#                  COMMON SETUP SECTION                           #
###################################################################


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def misc(self):
        requests.packages.urllib3.disable_warnings()

    # Connect to each device in the testbed
    @aetest.subsection
    def get_devices(self, testbed):
        genie_testbed = Genie.init(testbed)
        self.parent.parameters["testbed"] = genie_testbed
        device_list = []

        # Attempt to establish connection with each device
        for device in genie_testbed.devices.values():
            if device.os in ["iosxe", "nxos", "iosxr"]:
                log.info(banner("Connect to device '{d}'".format(d=device.name)))
                device_list.append(device)

        # Pass list of devices the to testcases
        self.parent.parameters.update(dev=device_list)




###################################################################
#                     TESTCASES SECTION                           #
###################################################################


class Connectivity_Verify(aetest.Testcase):
    """ Test if Device is reachable through all connections is functioning properly """

    @aetest.test
    def test_ssh(self):
        """ Verify device reachable through SSH """

        for dev in self.parent.parameters["dev"]:
            log.info(
                banner("Testing SSH Access to {}".format(dev.name))
            )

            # Retry loop, number of tries controlled by variable.
            for _ in range(MAX_RETRIES):
                try:
                    dev.connect(alias="admin", via="admin", learn_hostname=True)
                except Exception as e:
                    log.error("Attempt number {} to connect with SSH failed.".format(_ + 1))
                    log.error(e)
                else:
                    break
            # If unable to connect, fail test
            else:
                self.failed(
                    "Failed to establish SSH connection to '{}'".format(
                        dev.name
                    )
                )


    @aetest.test
    def test_netconf(self):
        """ Verify device reachable through NETCONF """

        for dev in self.parent.parameters["dev"]:
            if "netconf" in dev.connections:
                log.info(
                    banner("Testing NETCONF Access to {}".format(dev.name))
                )
                # Retry loop
                for _ in range(MAX_RETRIES):
                    try:
                        with manager.connect(
                                host = str(dev.connections.netconf.ip),
                                port = str(dev.connections.netconf.port),
                                username = dev.tacacs.username,
                                password = dev.passwords.tacacs,
                                hostkey_verify = False,
                                look_for_keys=False
                        ) as m:
                            log.info("NETCONF Connected is {}".format(m.connected))

                    # If unable to connect, fail test
                    except Exception as e:
                        log.error("Attempt number {} to connect with NETCONF failed.".format(_ + 1))
                        log.error(e)
                    else:
                        break
                # If unable to connect, fail test
                else:
                    self.failed(
                        "Failed to establish NETCONF connection to '{}'".format(
                            dev.name
                        )
                    )

    @aetest.test
    def test_restconf(self):
        """ Verify device reachable through RESTCONF.
            Device must support 8040 RFP RESTCONF for test to pass.
        """

        for dev in self.parent.parameters["dev"]:
            if "restconf" in dev.connections:
                log.info(
                    banner("Testing RESTCONF Access to {}".format(dev.name))
                )
                # Retry loop
                for _ in range(MAX_RETRIES):
                    try:
                        url = "https://{host}:{port}/.well-known/host-meta".format(
                            host=str(dev.connections.restconf.ip),
                            port=dev.connections.restconf.port
                            )
                        response = requests.get(url,
                                auth = (dev.tacacs.username, dev.passwords.tacacs),
                                verify = False
                               )
                        if response.status_code == 200:
                            log.info("RESTCONF Connected - Status Code: {}".format(
                                response.status_code
                                )
                            )
                        else:
                            self.failed(
                                "ERROR: RESTCONF Status Code is {} (should be 200).".format(
                                    response.status_code
                                )
                            )

                    # If unable to connect, fail test
                    except Exception as e:
                        log.error("Attempt number {} to connect with RESTCONF failed.".format(_ + 1))
                        log.error(e)
                    else:
                        break
                # If unable to connect, fail test
                else:
                    self.failed(
                        "Failed to establish RESTCONF connection to '{}'".format(
                            dev.name
                        )
                    )


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self):
        for dev in self.parent.parameters["dev"]:
            dev.disconnect_all()




if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
