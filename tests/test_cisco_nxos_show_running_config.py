from unittest import TestCase

from ttp import ttp

from . import DeviceFacts, DeviceVlan, DeviceInterface, IPv4


class TestCiscoNXOS(TestCase):
    maxDiff = None

    def setUp(self):
        with open("tests/configs/cisco_nxos_show_running_config.txt") as f:
            config = f.read()

        with open("ttp_templates/templates/cisco_nxos_show_running_config.ttp") as f:
            template = f.read()

        parser = ttp(data=config, template=template)
        parser.parse()
        self.result = parser.result()[0]

    def test_facts(self):
        self.assertEqual(
            self.result["facts"],
            DeviceFacts(
                hostname="nxos1",
                os_version="6.2(16)",
            ).model_dump(exclude={"serial_number", "domain_name"}),
        )

    def test_vlans(self):
        self.assertEqual(
            self.result["vlans"],
            [
                DeviceVlan(vlan_id=1).model_dump(),
                DeviceVlan(vlan_id=3, name="Management").model_dump(),
                DeviceVlan(vlan_id=4).model_dump(),
                DeviceVlan(vlan_id=5).model_dump(),
                DeviceVlan(vlan_id=50).model_dump(),
            ],
        )

    def test_interfaces(self):
        self.assertEqual(
            self.result["interfaces"],
            [
                DeviceInterface(
                    name="Vlan1",
                    description="",
                    enabled=False,
                    type="virtual",
                    ipv4=[
                        IPv4(ip="192.168.0.1/24").model_dump(exclude={"secondary"}),
                    ],
                ).model_dump(
                    exclude={
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "vlan_id",
                        "parent",
                        "mtu",
                        "duplex",
                        "label",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="Vlan3",
                    description="VLAN 3",
                    enabled=False,
                    type="virtual",
                ).model_dump(
                    exclude={
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "vlan_id",
                        "parent",
                        "mtu",
                        "duplex",
                        "label",
                        "ipv4",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="Vlan4",
                    description="",
                    enabled=True,
                    type="virtual",
                    ipv4=[
                        IPv4(ip="40.10.10.2/24").model_dump(exclude={"secondary"}),
                    ],
                    management=True,
                ).model_dump(
                    exclude={
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "vlan_id",
                        "parent",
                        "mtu",
                        "duplex",
                        "label",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="Port-channel1",
                    description="",
                    enabled=False,
                    type="lag",
                    mode="tagged-all",
                ).model_dump(
                    exclude={
                        "vlan_id",
                        "parent",
                        "mtu",
                        "duplex",
                        "label",
                        "ipv4",
                        "management",
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="Port-channel2",
                    description="",
                    enabled=False,
                    type="lag",
                    mode="access",
                    access_vlan=4,
                ).model_dump(
                    exclude={
                        "vlan_id",
                        "parent",
                        "mtu",
                        "duplex",
                        "label",
                        "ipv4",
                        "management",
                        "tagged_vlans",
                        "speed",
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="Port-channel3",
                    description="",
                    enabled=False,
                    type="lag",
                    mode="tagged-all",
                    access_vlan=5,
                ).model_dump(
                    exclude={
                        "vlan_id",
                        "parent",
                        "mtu",
                        "duplex",
                        "label",
                        "ipv4",
                        "management",
                        "tagged_vlans",
                        "speed",
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="Ethernet1/1",
                    description="",
                    enabled=True,
                    type="other",
                    mode="tagged",
                    tagged_vlans=[1, 2, 3],
                ).model_dump(
                    exclude={
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "vlan_id",
                        "parent",
                        "mtu",
                        "duplex",
                        "label",
                        "ipv4",
                        "management",
                        "access_vlan",
                        "speed",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="Ethernet1/2",
                    description="",
                    enabled=False,
                    type="other",
                    speed=1000,
                ).model_dump(
                    exclude={
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "vlan_id",
                        "parent",
                        "mtu",
                        "duplex",
                        "label",
                        "ipv4",
                        "management",
                        "access_vlan",
                        "tagged_vlans",
                        "lag_id",
                        "lacp_mode",
                        "lacp_max_bundle",
                        "mode",
                        "vrf",
                    }
                ),
                DeviceInterface(
                    name="Ethernet1/3",
                    description="",
                    enabled=True,
                    type="other",
                    lag_id=1,
                    lacp_mode="active",
                    mode="tagged-all",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "duplex",
                        "label",
                        "ipv4",
                        "management",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
            ],
        )
