import random
import re
#samMAC.py 
# I like to spoof macs to force xfinity to give me a new IP after disabling their routing function on the gateway and hooking up a router with mac spoofing capabilities.
def generate_mac_address():
    mac_octets = ["CC","E9","FA"]

    # Generate the remaining octets
    remaining_octets = [random.randint(0x00, 0xFF) for _ in range(3)]

    # Combine all the octets to form the MAC address
    mac_address = mac_octets + [format(octet, "02X") for octet in remaining_octets]

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
