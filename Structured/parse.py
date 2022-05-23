import yaml

example = open('example.yml', 'r')

structured_data = yaml.safe_load(example)

for switch in structured_data['devices']:
    print("Configuration for", switch)
    print("")
    for interface in structured_data['devices'][switch]['interfaces']:
        print("interface", interface)
        print("  ip address", structured_data['devices'][switch]['interfaces'][interface])
    print("")
    print("router bgp", structured_data['devices'][switch]['BGP']['ASN'])
    print("  router-id", structured_data['devices'][switch]['interfaces']['loopback0'])

