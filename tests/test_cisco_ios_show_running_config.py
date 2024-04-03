from unittest import TestCase

from ttp import ttp

from . import DeviceFacts, DeviceVRF, DeviceInterface, IPv4


class TestCiscoIOS(TestCase):
    maxDiff = None

    def setUp(self):
        with open("tests/configs/cisco_ios_show_running_config.txt") as f:
            config = f.read()

        with open("ttp_templates/templates/cisco_ios_show_running_config.ttp") as f:
            template = f.read()

        parser = ttp(data=config, template=template)
        parser.parse()
        self.result = parser.result()[0]

    def test_facts(self):
        self.assertEqual(
            self.result["facts"],
            DeviceFacts(
                hostname="ios1",
                os_version="15.5",
                domain_name="example.com",
            ).model_dump(exclude={"serial_number"}),
        )

    def test_vrfs(self):
        self.assertEqual(
            self.result["vrf"],
            [
                DeviceVRF(name="VRF1").model_dump(),
                DeviceVRF(name="VRF2").model_dump(),
            ],
        )

    def test_interfaces(self):
        self.assertEqual(
            self.result["interfaces"],
            [
                DeviceInterface(
                    name="Tunnel1",
                    type="virtual",
                    description="Tunnel1 ---> ISP1",
                    enabled=True,
                    ipv4=[
                        IPv4(ip="100.100.100.10/31").model_dump(exclude={"secondary"}),
                    ],
                ).model_dump(
                    exclude={
                        "label",
                        "parent",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "duplex",
                        "lacp_mode",
                        "lag_id",
                        "lacp_max_bundle",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="GigabitEthernet0/0/0",
                    type="other",
                    enabled=True,
                    ipv4=[
                        IPv4(ip="200.200.200.200/29").model_dump(exclude={"secondary"}),
                    ],
                ).model_dump(
                    exclude={
                        "label",
                        "parent",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "duplex",
                        "lacp_mode",
                        "lag_id",
                        "lacp_max_bundle",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="GigabitEthernet0/0/1",
                    type="other",
                    enabled=False,
                    description="LAN",
                ).model_dump(
                    exclude={
                        "label",
                        "parent",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "duplex",
                        "lacp_mode",
                        "lag_id",
                        "lacp_max_bundle",
                        "vrf",
                        "ipv4",
                    }
                ),
                DeviceInterface(
                    name="GigabitEthernet0/0/1.10",
                    type="virtual",
                    enabled=True,
                    parent="GigabitEthernet0/0/1",
                    access_vlan=10,
                    mode="access",
                    vrf="VRF1",
                    ipv4=[
                        IPv4(ip="10.10.10.1/24").model_dump(exclude={"secondary"}),
                        IPv4(ip="20.20.20.1/24", secondary=True).model_dump(),
                    ],
                ).model_dump(
                    exclude={
                        "label",
                        "mtu",
                        "management",
                        "tagged_vlans",
                        "speed",
                        "duplex",
                        "lacp_mode",
                        "lag_id",
                        "lacp_max_bundle",
                    }
                ),
            ],
        )
