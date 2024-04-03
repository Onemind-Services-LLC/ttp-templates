from unittest import TestCase

from ttp import ttp

from . import ASAFacts, ASAInterface, IPv4, DeviceAclStandard


class TestCiscoASA(TestCase):
    maxDiff = None

    def setUp(self):
        with open("tests/configs/cisco_asa_show_running_config.txt") as f:
            config = f.read()

        with open("ttp_templates/templates/cisco_asa_show_running_config.ttp") as f:
            template = f.read()

        parser = ttp(data=config, template=template)
        parser.parse()
        self.result = parser.result()[0]

    def test_facts(self):
        self.assertEqual(
            self.result["facts"],
            ASAFacts(
                serial_number="SN001",
                os_version="9.12(4)",
                hostname="ASA5585X",
                domain_name="example.local",
                boot_image="disk0:/asa9-12-4-smp-k8.bin",
                asdm_image="disk0:/asdm-7131-101.bin",
            ).model_dump(),
        )

    def test_interfaces(self):
        self.assertEqual(
            self.result["interfaces"],
            [
                ASAInterface(
                    name="GigabitEthernet0/0",
                    description="",
                    label="",
                    type="other",
                    enabled=True,
                    security_level=None,
                    duplex="full",
                    lag_id=1,
                    lacp_mode="active",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="GigabitEthernet0/1",
                    description="",
                    label="",
                    type="other",
                    enabled=True,
                    security_level=None,
                    duplex="full",
                    lag_id=1,
                    lacp_mode="active",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="GigabitEthernet0/2",
                    description="",
                    label="",
                    type="other",
                    enabled=True,
                    security_level=None,
                    duplex="full",
                    lag_id=1,
                    lacp_mode="active",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="GigabitEthernet0/3",
                    description="",
                    label="",
                    type="other",
                    enabled=True,
                    security_level=None,
                    duplex="full",
                    lag_id=1,
                    lacp_mode="active",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="GigabitEthernet0/4",
                    description="",
                    label="",
                    type="other",
                    enabled=True,
                    security_level=None,
                    duplex="full",
                    lag_id=1,
                    lacp_mode="active",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="GigabitEthernet0/5",
                    description="",
                    label="",
                    type="other",
                    enabled=True,
                    security_level=None,
                    duplex="full",
                    lag_id=1,
                    lacp_mode="active",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="GigabitEthernet0/6",
                    description="",
                    label="",
                    type="other",
                    enabled=True,
                    security_level=None,
                    duplex="full",
                    lag_id=1,
                    lacp_mode="active",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="GigabitEthernet0/7",
                    description="",
                    label="",
                    type="other",
                    enabled=True,
                    security_level=None,
                    duplex="full",
                    lag_id=1,
                    lacp_mode="active",
                    parent="Port-channel1",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="Management0/0",
                    description="",
                    label="management",
                    type="other",
                    enabled=True,
                    security_level=100,
                    duplex="auto",
                    mtu=1500,
                    ipv4=[
                        IPv4(ip="10.10.10.1/24").model_dump(exclude={"secondary"}),
                        IPv4(ip="20.20.20.1/24", secondary=True).model_dump(),
                    ],
                ).model_dump(
                    exclude={
                        "lacp_max_bundle",
                        "lacp_mode",
                        "lag_id",
                        "parent",
                        "vlan_id",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="Management0/1",
                    description="",
                    label="",
                    type="other",
                    enabled=False,
                    security_level=None,
                    duplex="auto",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "lacp_mode",
                        "lag_id",
                        "parent",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="TenGigabitEthernet0/8",
                    description="",
                    label="",
                    type="other",
                    enabled=False,
                    security_level=None,
                    duplex="auto",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "lacp_mode",
                        "lag_id",
                        "parent",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="TenGigabitEthernet0/9",
                    description="",
                    label="",
                    type="other",
                    enabled=False,
                    security_level=None,
                    duplex="auto",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "lacp_mode",
                        "lag_id",
                        "parent",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="Port-channel1",
                    description="LACP1",
                    label="",
                    type="lag",
                    enabled=True,
                    security_level=None,
                    duplex="auto",
                    lacp_max_bundle="8",
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_mode",
                        "lag_id",
                        "parent",
                        "vlan_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
                ASAInterface(
                    name="Port-channel1.100",
                    description="",
                    label="",
                    type="virtual",
                    enabled=True,
                    security_level=None,
                    duplex="auto",
                    parent="Port-channel1",
                    vlan_id=100,
                ).model_dump(
                    exclude={
                        "ipv4",
                        "lacp_max_bundle",
                        "lacp_mode",
                        "lag_id",
                        "mtu",
                        "management",
                        "mode",
                        "access_vlan",
                        "tagged_vlans",
                        "speed",
                        "vrf",
                    }
                ),
            ],
        )

    def test_objects(self):
        self.assertEqual(
            self.result["objects"]["network_objects"],
            {
                "obj_net_1": {
                    "description": "Sample network object",
                    "ip": "192.168.1.1",
                    "nat_rule": {
                        "source_interface": "any",
                        "destination_interface": "outside",
                        "type": "static",
                        "interface": "100.100.100.10",
                        "protocol": "tcp",
                        "source_port": 80,
                        "destination_port": 80,
                    },
                }
            },
        )

        self.assertEqual(
            self.result["objects"]["service_objects"],
            {"obj_svc_1": {"description": "", "protocol": "tcp", "port": 80}},
        )

        self.assertEqual(
            self.result["objects"]["range_objects"],
            {
                "obj_range_1": {
                    "description": "",
                    "begin_ip": "10.0.0.1",
                    "end_ip": "10.0.0.254",
                }
            },
        )

        self.assertEqual(
            self.result["objects"]["fqdn_objects"],
            {"obj_fqdn_1": {"description": "", "fqdn": "www.example.com"}},
        )

        self.assertEqual(
            self.result["objects"]["subnet_objects"],
            {
                "obj_subnet_1": {
                    "description": "",
                    "ip": "192.168.0.0/24",
                }
            },
        )

    def test_acl_standard(self):
        self.assertEqual(
            self.result["access_lists"]["standard"],
            {
                "VTY_ADMINS": [
                    DeviceAclStandard(
                        action="permit",
                        prefix_ip="10.10.10.0",
                        prefix_mask="255.255.255.0",
                    ).model_dump(),
                ]
            },
        )

    def test_acl_group(self):
        self.assertEqual(
            self.result["access_groups"],
            {
                "acl_name": "ACL-OUT",
                "direction": "out",
                "interface": "outside",
            },
        )

    def test_routes(self):
        self.assertEqual(
            self.result["routes"],
            [
                {
                    "interface": "outside",
                    "network": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "gateway": "100.100.10.10",
                    "metric": 1,
                },
                {
                    "interface": "management",
                    "network": "10.10.10.0",
                    "mask": "255.255.255.0",
                    "gateway": "10.10.20.0",
                    "metric": 10,
                },
            ],
        )
