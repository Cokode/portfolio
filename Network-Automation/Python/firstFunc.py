import sys
import requests
from requests.auth import HTTPBasicAuth
from info import USERNAME, PASSWORD, URL


## function to get the interfaces from the API and print them.
def printInterfaces():

	try:

		response = requests.get(
			URL,
			headers={'Accept': 'application/yang-data+json'},
			auth=HTTPBasicAuth(USERNAME, PASSWORD),
			verify=False
		)

		data = response.json()
		# print(data)
		printREsult(data)
		
	except KeyboardInterrupt as e: 
		print('print there was an error', e)
		sys.exit()


## A helperfunction to print the result of the API call in a formatted way.
## that is easy to read and understand. (focus on only enabled interfaces)
def printREsult(result):
		interfaces = result["ietf-interfaces:interfaces"]["interface"]

		for intf in interfaces:
			if intf["enabled"] != False:
				print("Name:", intf["name"])
				print("description:", intf.get("description"))
				print("Type:", intf.get("type"))
				print("enabled:", intf.get("enabled"))
				print("ipv4:", intf.get("ietf-ip:ipv4"))
				print("ipv6:", intf.get("ietf-ip:ipv6"))
				print("----")


## main function to call the printInterfaces function.
if __name__ == "__main__":
	printInterfaces()