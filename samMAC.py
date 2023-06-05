import random
import re
#samMAC.py 
# I like to spoof macs to force xfinity to give me a new IP after disabling their routing function on the gateway and hooking up a router with mac spoofing capabilities.
def generate_mac_address():
    samsung_octets = ["CC","E9","FA"]
    cisco_octets = ["90", "88", "55"]
    amazon_octets =  ["28", "73", "F6"]
    apple_octets  = ["20", "15", "82"]
    dell_octets = ["78", "2B", "CB"]
    zyxel_octets = ["F8", "0D", "A9"]
    juniper_octets = ["50", "C5", "8D"]
    sony_octets = ["AC", "80", "0A"]
    ms_octets =   ["FC", "8C"," 11"]

    octets = [
	samsung_octets,
	cisco_octets,
	amazon_octets,
	apple_octets,
	dell_octets,
	zyxel_octets,
	juniper_octets,
	sony_octets,
        ms_octets
	]

    length = len(octets) -1 # raw length of array with -1 computer logic for future adapability
    prefix = octets[random.randint(0, length)] 

    # Generate the remaining octets
    remaining_octets = [random.randint(0x00, 0xFF) for _ in range(3)]

    # Combine all the octets to form the MAC address
    mac_address = prefix + [format(octet, "02X") for octet in remaining_octets]

    return ":".join(mac_address)

def validate_mac_address(mac_address):
    # Regular expression pattern for MAC address validation
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return bool(re.match(pattern, mac_address))

# Generate a random MAC address and validate it
mac_address = generate_mac_address()
while not validate_mac_address(mac_address):
    mac_address = generate_mac_address()

print(mac_address)
