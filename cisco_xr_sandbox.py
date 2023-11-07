#!/home/nincepython/.venv/bin/python3


import netmiko
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    # 'ip': 'IP_ADDRESS',
    'username': 'admin',
    'password': 'C1sco12345',
}

# Establish an SSH connection to the device
connection = ConnectHandler(**device)

# Execute "show ip interface brief" command
output = connection.send_command("show ip interface brief")

# Print the output
print(output)

# Close the SSH connection
connection.disconnect()
