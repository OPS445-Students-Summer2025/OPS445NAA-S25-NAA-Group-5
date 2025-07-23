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


    parts = ip.split(".")

    if len(parts) == 4:			
        for part in parts:
            if part.isdigit():		
                number = int(part)	
                if number < 0 or number > 255:	
                    print(f' Oops! {number} is out of range (0-255).')
                    return False
            else:
                print(f"Oops! '{part}' is not a number.")	
                return False
        print(f'Great! {ip} is a valid IPv4 address.')	
        return True
    else:
        print('Oops! IP address must have 4 numbers separated by dots.')	
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
                                        new_lines.append(line)
                        else:
                                new_lines.append(line)
                else:
                        new_lines.append(line)


        # Write Changes back to the file
        with open(file_path, 'w') as file:
                file.writelines(new_lines)

        # Message
        print(f"Network configuration updated to {mode} mode.")


# ----------------------------
# Function 4: Test Connectivity (Ping)
# ----------------------------

def test_ping(target):
    """
    Ping a target IP or hostname to test connectivity.
    Sends 2 ICMP echo requests using 'ping -c 2'.
    """
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
    else:
        print("Ping successful!")
 
    # TODO: Use subprocess to run 'ping -c 2 <target>' and print result
    pass
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
