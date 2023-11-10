import sys
from netmiko import ConnectHandler

# Print the command-line arguments passed to the script
print("Command-line arguments:", sys.argv)

# RUAJI NE JENKINS KREDENCIALET

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py ENTER_USERNAME ENTER_PASSWORD")
    sys.exit(1)

# Extracting username and password from command-line arguments
username = sys.argv[1]
password = sys.argv[2]

# Print the parameters
print("Username qe kemi perdorur si argument eshte: ", username)
print("Password qe kemi regjistruar ne jenkins eshte :", password)

device = {
    'device_type': 'cisco_xr',
    'host': 'sandbox-iosxr-1.cisco.com',
    'username': username,
    'password': password,
    #'username': 'admin',
    #'password': 'C1sco12345',
}

# Establish an SSH connection to the device
ssh_active = ConnectHandler(**device)
print(ssh_active.find_prompt())

# Execute "show version" command
output = ssh_active.send_command("show version")

# Print the output
print(output)
output = ssh_active.send_command("show ip int brief ")
# Print the output
print(output)


# Close the SSH connection
ssh_active.disconnect()
