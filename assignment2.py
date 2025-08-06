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
    pass


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
    # TODO: Use shutil to copy the file safely
    pass


# ----------------------------
# Function 3: Change Network Mode (static/dhcp)
# ----------------------------
def change_network_mode(file_path, mode, ip=None):
    """
    Changes the network mode to either static or dhcp.

    Arguments:
        file_path (str): Path to the network config file.
        mode (str): 'static' or 'dhcp'.
        ip (str, optional): Required if mode is static.

    Behavior:
        - Backup the original file first.
        - Modify lines related to BOOTPROTO and IPADDR.
        - Save the changes.
    """
    # TODO: Read the file, modify lines, and write back changes
    pass


# ----------------------------
# Function 4: Test Connectivity (Ping)
# ----------------------------

def test_ping(target):
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

# ----------------------------
# Main Function with Argument Parser
# ----------------------------
def main():
    """
    Main function to handle command line arguments and call appropriate functions.

    Commands supported:
        - validate <ip>
        - backup <file_path>
        - change <file_path> <mode> [--ip <ip_address>]
        - ping [--target <ip>]
    """
    parser = argparse.ArgumentParser(description="Network Configuration Tool")

    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # Subcommand: validate
    parser_validate = subparsers.add_parser("validate", help="Validate an IP address")
    parser_validate.add_argument("ip", help="IP address to validate")

    # Subcommand: backup
    parser_backup = subparsers.add_parser("backup", help="Backup a network config file")
    parser_backup.add_argument("file", help="Path to the file to back up")

    # Subcommand: change
    parser_change = subparsers.add_parser("change", help="Change network mode (static/dhcp)")
    parser_change.add_argument("file", help="Path to the config file")
    parser_change.add_argument("mode", choices=["static", "dhcp"], help="Network mode to set")
    parser_change.add_argument("--ip", help="Static IP address (required for static mode)")

    # Subcommand: ping
    parser_ping = subparsers.add_parser("ping", help="Ping a target to test connectivity")
    parser_ping.add_argument("--target", default="8.8.8.8", help="Target IP to ping")

    args = parser.parse_args()

    # TODO: Call the appropriate function based on command
    if args.command == "validate":
        pass  # Call validate_ip()

    elif args.command == "backup":
        pass  # Call backup_file()

    elif args.command == "change":
        pass  # Call change_network_mode()

    elif args.command == "ping":
        pass  # Call test_ping()

    else:
        parser.print_help()


# ----------------------------
# Entry Point
# ----------------------------
if __name__ == "__main__":
    main()
=======
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
... 
... # ----------------------------
... # Main Function with Argument Parser
... # ----------------------------
... def main():
...     """
...     Main function to handle command line arguments and call appropriate functions.
... 
...     Commands supported:
...         - validate <ip>
...         - backup <file_path>
...         - change <file_path> <mode> [--ip <ip_address>]
...         - ping [--target <ip>]
...     """
    parser = argparse.ArgumentParser(description="Network Configuration Tool")

    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # Subcommand: validate
    parser_validate = subparsers.add_parser("validate", help="Validate an IP address")
    parser_validate.add_argument("ip", help="IP address to validate")

    # Subcommand: backup
    parser_backup = subparsers.add_parser("backup", help="Backup a network config file")
    parser_change = subparsers.add_parser("change", help="Change network mode (static/dhcp)")
    parser_change.add_argument("file", help="Path to the config file")
    parser_change.add_argument("mode", choices=["static", "dhcp"], help="Network mode to set")
    parser_change.add_argument("--ip", help="Static IP address (required for static mode)")

    # Subcommand: ping
    parser_ping = subparsers.add_parser("ping", help="Ping a target to test connectivity")
    parser_ping.add_argument("--target", default="8.8.8.8", help="Target IP to ping")

    args = parser.parse_args()

    # TODO: Call the appropriate function based on command
    if args.command == "validate":
        pass  # Call validate_ip()

    elif args.command == "backup":
        pass  # Call backup_file()

    elif args.command == "change":
        pass  # Call change_network_mode()

    elif args.command == "ping":
        pass  # Call test_ping()

    parser_backup.add_argument("file", help="Path to the file to back up")

    # Subcommand: change
    parser_change = subparsers.add_parser("change", help="Change network mode (static/dhcp)")
    parser_change.add_argument("file", help="Path to the config file")
    parser_change.add_argument("mode", choices=["static", "dhcp"], help="Network mode to set")
    parser_change.add_argument("--ip", help="Static IP address (required for static mode)")

    # Subcommand: ping
    parser_ping = subparsers.add_parser("ping", help="Ping a target to test connectivity")
    parser_ping.add_argument("--target", default="8.8.8.8", help="Target IP to ping")

    args = parser.parse_args()

    if args.command == "validate":
        validate_ip(args.ip)

    elif args.command == "backup":
        try:
            backup_file(args.file)
        except FileNotFoundError as e:
            print(f"ERROR: {e}")

    elif args.command == "change":
        if args.mode == "static":
            if not args.ip:
                print("ERROR: Static requires an IP address.")
                return
            if not validate_ip(args.ip):
                print("ERROR: invalid IP provided.")
                return
        change_network_mode(args.file, args.mode, ip=args.ip)
        # Restart NetworkManager to apply changes
        print("Restarting NetworkManager to apply new changes")
        res = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Failed to restart NetworkManager: {res.stderr.strip()}")
        else:
            print("NetworkManager restarted successfully.")

    elif args.command == "ping":
        if not test_ping(args.target):
            print("Ping failed: there may be an issue with the current network configuration.")
            # Attempt to restore NetworkManager config from backup
            orig_path = "/etc/NetworkManager/NetworkManager.conf"
            backup_path = "/etc/NetworkManager/NetworkManager.conf.bak"
            if os.path.isfile(backup_path):
                try:
                    if os.path.isfile(orig_path):
                        os.remove(orig_path)
                        print(f"Deleted current config at {orig_path}.")
                    shutil.copy2(backup_path, orig_path)
                    print(f"Restored backup configuration from {backup_path} to {orig_path}.")
                    # Restart to apply restored config
                    print("Restarting NetworkManager to apply new changes.")
                    res = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"], capture_output=True, text=True)
                    if res.returncode != 0:
                        print(f"ERROR: Could not restart NetworkManager.\n{res.stderr.strip()}")
                    else:
                        print("NetworkManager restarted successfully.")
                except PermissionError:
                    print("ERROR: Could not restore backup. Try running with elevated privileges.")
                except OSError as e:
                    print(f"ERROR: Failed to restore backup: {e}")
            else:
                print(f"No backup found at {backup_path}. Cannot restore configuration.")
    else:
        parser.print_help()


# ----------------------------
# Entry Point
# ----------------------------
if __name__ == "__main__":
    main()
>>>>>>> 80c92d338f71f8e8ef769532e3b9ac40cc226555
