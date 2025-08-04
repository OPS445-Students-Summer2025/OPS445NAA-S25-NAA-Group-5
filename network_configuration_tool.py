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
