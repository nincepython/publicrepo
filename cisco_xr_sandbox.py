#!/home/nincepython/.venv/bin/python3


import netmiko
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    # 'ip': 'IP_ADDRESS',
    'username': 'admin',
    #'username': input("Enter your username: \n"),
    'password': 'C1sco12345',
}

# Establish an SSH connection to the device
ssh_active = ConnectHandler(**device)
print(ssh_active.find_prompt())

# Execute "show ip interface brief" command
#output = ssh_active.send_command("show ip interface brief")
output = ssh_active.send_command("show version")

# Print the output
print(output)

# Close the SSH connection
ssh_active.disconnect()
