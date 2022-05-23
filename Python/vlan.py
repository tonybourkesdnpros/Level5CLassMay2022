# This is a script to configure a large number of VLANs via pyeAPI

import pyeapi

switches = ['leaf1-DC1', 'leaf2-DC1', 'leaf3-DC1', 'leaf4-DC1']

vlan_start = 1000

for switch in switches:
    vlan_id = vlan_start
    print(switch)
    while vlan_id < 2000:
        print("deleting vlan", vlan_id)
        vlan_id = vlan_id + 1
        connect = pyeapi.connect_to(switch)
        result = connect.api("vlans").delete(vlan_id)