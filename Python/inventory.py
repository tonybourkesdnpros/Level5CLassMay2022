
from cvprac.cvp_client import CvpClient
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp = "192.168.0.5"
cvp_user = "arista"
cvp_pw = "aristazpjp"

client = CvpClient()

client.connect([cvp], cvp_user, cvp_pw)

inventory = client.api.get_inventory()

for item in inventory:
    print(item['hostname'])