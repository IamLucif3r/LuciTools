#!/usr/bin/ python

#Automating MAC Address changing
import subprocess
import optparse 
import re

def get_arguments():
	parser = optparse.OptionParser() 
	parser.add_option("-i","--interface",dest="interface", help="Interface to change its MAC Address")
	parser.add_option("-m","--mac",dest="new_mac", help="New MAC Address")
	# Option and Arguments are not Keywords
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an Interface, use --help for more info.")
	elif not options.new_mac:
		parser.error("[-] Please specify an MAC Address, use --help for more info.")
	return options
	
def change_mac(interface,new_mac):
	print("[*] Changing MAC Address for "+interface+" to "+new_mac)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw","ether",new_mac])
	subprocess.call(["ifconfig", interface, "up"])

def get_curr_mac(interface):
	ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("[-] Cannot get MAC Address. Check your interface")


options = get_arguments()
curr_mac = get_curr_mac(options.interface)
print("[+] Current MAC Address : "+str(curr_mac))
change_mac(options.interface,options.new_mac)

curr_mac = get_curr_mac(options.interface)
if curr_mac == options.new_mac:
	print("[+] MAC Address successfully changed to "+curr_mac)
else:
	print("[-] MAC Address could not change")