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
def validate_ip(ip, subnet):
    """
    Checks if the given IP address is valid (IPv4).
    
    Arguments:
        ip (str): The IP address to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    parts = ip.split(".") 

    if len(parts) != 4:
        print("Oops! IP address must have 4 numbers separated by dots.")   
        return False

    for part in parts:
        if not part.isdigit():
            print(f"Oops! '{part}' is not a number.")
            return False
        if part.startswith("0") and len(part) > 1:
            print(f"Oops! '{part}' should not have leading zeros.")
            return False
        number = int(part)
        if number < 0 or number > 255:
            print(f"Oops! {number} is out of range (0–255).")
            return False

    # Validate subnet if provided
    try:
        subnet_int = int(subnet)
        if subnet_int < 0 or subnet_int > 32:
            print("Oops! Subnet mask must be between 0 and 32.")
            return False
    except (ValueError, TypeError):
        print("Oops! Subnet mask must be an integer.")
        return False
    
    print(f"Great! {ip}/{subnet} is a valid IPv4 address with subnet.")
    return True


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
