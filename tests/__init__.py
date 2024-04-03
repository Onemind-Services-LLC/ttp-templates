from typing import Optional, Literal

from pydantic import BaseModel

__all__ = [
    "ASAFacts",
    "ASAInterface",
    "DeviceAclStandard",
    "DeviceFacts",
    "DeviceInterface",
    "DeviceVlan",
    "DeviceVRF",
    "IPv4",
]


class DeviceFacts(BaseModel):
    serial_number: Optional[str] = ""
    os_version: str
    hostname: str
    domain_name: Optional[str] = ""


class ASAFacts(DeviceFacts):
    boot_image: str
    asdm_image: str


class IPv4(BaseModel):
    ip: str
    secondary: Optional[bool] = False


class DeviceInterface(BaseModel):
    name: str
    description: Optional[str] = ""
    enabled: bool
    label: Optional[str] = ""
    type: Literal["other", "virtual", "lag", "bridge"]
    duplex: Literal["auto", "full", "half"] = "auto"
    lag_id: Optional[int] = None
    lacp_mode: Optional[str] = ""
    lacp_max_bundle: Optional[str] = ""
    vlan_id: Optional[int] = None
    ipv4: Optional[list[dict]] = None
    parent: Optional[str] = ""
    mtu: Optional[int] = None
    management: Optional[bool] = False
    mode: Literal["", "access", "tagged", "tagged-all"] = ""
    access_vlan: Optional[int] = None
    tagged_vlans: Optional[list[int]] = None
    speed: Optional[int] = None
    vrf: Optional[str] = None


class ASAInterface(DeviceInterface):
    security_level: Optional[int] = None


class DeviceAclStandard(BaseModel):
    action: Literal["permit", "deny"]
    prefix_ip: str
    prefix_mask: str


class DeviceVlan(BaseModel):
    vlan_id: int
    name: Optional[str] = None


class DeviceVRF(BaseModel):
    name: str
