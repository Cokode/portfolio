import requests
from requests.auth import HTTPBasicAuth

url = "https://devnetsandboxiosxec9k.cisco.com/restconf/data/ietf-interfaces:interfaces"

response = requests.get(
    url,
    auth=HTTPBasicAuth("collinsama343", "f2k7V_a0Dm-L"),
    headers={"Accept": "application/yang-data+json"},
    verify=False
)

print(response.status_code)
print(response.text)
