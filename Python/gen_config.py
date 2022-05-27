import yaml



device_list = ['leaf1-DC1', 'leaf2-DC1']

config_file = open('config.yml', 'r')

config = yaml.safe_load(config_file)


    # for device in device_list:
    #     print("Interface config for", device)
    #     print("")
    #     for interface in config['devices'][device]['interfaces']:
    #         print("interface", interface)
    #         print("   ip address", config['devices'][device]['interfaces'][interface])
    #     print("")

for pancake in config['devices']['leaf1-DC1']['interfaces']:
    print("interface", pancake)
    ip = config['devices']['leaf1-DC1']['interfaces'][pancake]
    print("ip address", ip)