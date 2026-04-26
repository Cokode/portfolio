import requests
import json
from requests.auth import HTTPBasicAuth

device = "https://devnetsandboxiosxec9k.cisco.com/restconf/data/Cisco-IOS-XE-native:native/vlan"

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

payload = {
    "Cisco-IOS-XE-native:vlan": {
        "id": 20,
        "name": "API_VLAN"
    }
}

response = requests.post(
    device,
    data=json.dumps(payload),
    headers=headers,
    auth=HTTPBasicAuth("collinsama343", "f2k7V_a0Dm-L"),
    verify=False
)

print(response.status_code)
print(response.text)
