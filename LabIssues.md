# CVP Non-responsive after applying OSPF underlay configlets

There appears to be some sort of looping issue going on (not sure if it's data plane or control plane at this point). It consumes a lot of CPU which makes CVP unresponsive. 

Here's how to fix it: 

log into each leaf (leaf1-4-DC1, borderleaf1-2-DC1, same for DC2) and run this command: 

    conf
    int e3-5
    shut
    
Same for the spines (spines1-3-DC1, spines1-3-DC2)

    conf
    int e2-7
    shut
    
This shuts off all the connected interfaces. Wait about 20 minutes, then following the instructions in this repository: https://github.com/tonybourkesdnpros/ATD-Reset-Level5 (or just remove the configlets for OSPF manually)
