# assignment2.py

"""
Assignment 2 - Network Configuration Tool
This script provides :
- Validate an IP address
- Change network configuration (static or dhcp)
- Backup network config files
- Test connectivity using ping
All functionality should be implemented using Python standard libraries only.
"""

import argparse
import os
import shutil
import subprocess

# ----------------------------
# Function 1: Validate IP Address
# ----------------------------

def validate_ip(ip):
    """
    Checks if the given IP address is valid (IPv4).
    
    Arguments:
        ip (str): The IP address to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    # TODO: Implement logic to check IP address format (e.g., 192.168.0.1)

    parts = ip.split(".")  				# Split IP by dots into 4 parts

    if len(parts) == 4:  				# Check if there are exactly 4 parts
        for part in parts:  				# Loop through each part
            if part.isdigit():  			# Check if part is a number
                if part.startswith("0") and len(part) > 1:  # Reject leading zeros (e.g., '01')
                    print(f"Oops! '{part}' should not have leading zeros.")
                    return False
                number = int(part)  			# Convert part to integer
                if number < 0 or number > 255:  	# Check range 0–255
                    print(f"Oops! {number} is out of range (0–255).")
                    return False
            else:  					# Part is not a number
                print(f"Oops! '{part}' is not a number.")
                return False
        print(f"Great! {ip} is a valid IPv4 address.")  # All checks passed
        return True
    else:  						# Not exactly 4 parts
        print("Oops! IP address must have 4 numbers separated by dots.")
        return False

# ----------------------------
# Function 2: Backup Config File
# ----------------------------
def backup_file(file_path):
    """
    Creates a backup of the given network config file.

    Arguments:
        file_path (str): Path to the config file to back up.

    Behavior:
        - Check if the file exists.
        - Copy it to a new file with '.bak' extension.
    """


    response = input("Would you like to create a backup of your network config file? (Y/N): ")
    response = response.strip().lower()

    if response not in ("y", "yes"):
        print("Backup skipped.")
        return None

    # Proceed with backup
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    backup_dir = os.path.expanduser("~/backups")
    os.makedirs(backup_dir, exist_ok=True)

    backup_path = os.path.join(backup_dir, os.path.basename(file_path) + ".bak")

    try:
        shutil.copy2(file_path, backup_path)
    except PermissionError as exc:
        # This could happen if you can't read the source file.
        print(f"Backup failed due to permissions: {exc}")
        return None
    except OSError as exc:
        print(f"Backup failed: {exc}")
        return None

    print(f"Backup created at: {backup_path}")
    return backup_path




    # TODO: Use shutil to copy the file safely
    pass


# ----------------------------
# Function 3: Change Network Mode (static/dhcp)
# ----------------------------
def change_network_mode(file_path, mode, ip=None):

        # Check if the file exists
        if not os.path.exists(file_path):
                print(f"Error: File {file_path} does not exist.")
                return

        # Validate static mode input
        if mode == "static" and not ip:
                print("Error: Static mode requires an IP address.")
                return

        # Backup file
        backup_file(file_path)

        # Read the file
        with open(file_path, 'r') as file:
                lines = file.readlines()

        # Tracking
        new_lines = []
        in_ipv4 = False

        # Process each line
        for line in lines:
                stripped = line.strip()

        # Check ipv4
                if stripped == "[ipv4]":
                        in_ipv4 = True
                        new_lines.append(line)
                        continue

                elif stripped.startswith("[") and stripped != "[ipv4]":
                        in_ipv4 = False



        # Modify ipv4
                if in_ipv4:
                        if stripped.startswith("method="):
                                if mode =="dhcp":
                                        new_lines.append("method=auto\n")
                                else:
                                        new_lines.appned("method=manual\n")
                        elif stripped.startswith("address1="):
                                if mode == "static" and ip:
                                        new_lines.append(f"address1={ip}\n")
                                elif mode == "dchp":

                                        continue

                                else:
                                        new_lines.append(line)
                        elif stripped.startswith("dns="):
                                if mode == "static":
                                new_lines.append("dns=8.8.8.8.8;\n"
                                elif mode == "dhcp":

                                        continue
                                else:
...                                         new_lines.append(line)
...                         else:
...                                 new_lines.append(line)
...                 else:
...                         new_lines.append(line)
... 
... 
...         # Write Changes back to the file
...         with open(file_path, 'w') as file:
...                 file.writelines(new_lines)
... 
...         # Message
...         print(f"Network configuration updated to {mode} mode.")
... 
... 
... # ----------------------------
... # Function 4: Test Connectivity (Ping)
... # ----------------------------
... 
... def test_ping(target):
...     """
...     Ping a target IP or hostname to test connectivity.
...     Sends 2 ICMP echo requests using 'ping -c 2' on Linux.
...     Returns True if ping is successful, False otherwise.
...     """
...     print(f"\n📡 Pinging {target} using ping...\n")
... 
...     try:
...         # For Linux/Mac
...         result = subprocess.run(['ping', '-c', '2', target], capture_output=True, text=True)
...         
...         # Uncomment this for Windows instead:
...         # result = subprocess.run(['ping', '-n', '2', target], capture_output=True, text=True)
... 
...         # Show ping output
...         print(result.stdout)
... 
...         if result.returncode == 0:
...             print("Ping successful!")
...             return True
...         else:
...             print("Ping failed: No response from target.")
...             return False
... 
...     except TypeError:
...         print("Invalid input: target must be a string.")
...         return False
    """
    Pings a target IP address to test internet/network connectivity.

    Arguments:
        target (str): The IP address or hostname to ping.

    Behavior:
        - Use subprocess to run 'ping' command.
        - Show output.
    """

    try:
        print(f"\n📡 Pinging {target} using  ping...\n")

        # Use '-c 2' for 2 pings on Linux
        result = subprocess.run(['ping', '-c', '2', target], capture_output=True, text=True)

        # Run the ping command on Windows
        # result = subprocess.run(['ping', '-n', '2', target], capture_output=True, text=True)
    
        # Show ping command output
        print(result.stdout)

        # Check if ping was unsuccessful
        if result.returncode != 0:
            print("Ping failed: No response from target.")
            return False
        else:
            print("Ping successful!")
            return True
    except TypeError:
         print("Invalid input: target must be a string.")
         return False

... 
... # ----------------------------
... # Main Function with Argument Parser
@@ -341,3 +348,4 @@
# ----------------------------
if __name__ == "__main__":
    main()