#!/usr/bin/env python3
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
    # Proceed with backup
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    backup_dir = "/etc/NetworkManager/system-connections"
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

    

# ----------------------------
# Function 3: Change Network Mode (static/dhcp)
# ----------------------------

def change_network_mode(file_path, mode, ip=None, subnet=None):
    """
    Changes the network mode to either static or dhcp.

    Arguments:
        file_path (str): Path to the network config file.
        mode (str): 'static' or 'dhcp'.
        ip (str, optional): Required if mode is static.

    Behavior:
        - Backup the original file first.
        - Modify lines related to IP method, address, and DNS.
        - Save the changes.
    """

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        if os.path.exists("/run/NetworkManager/system-connections/Wired connection 1.nmconnection"):
            shutil.copy2("/run/NetworkManager/system-connections/Wired connection 1.nmconnection", "/etc/NetworkManager/system-connections/Wired connection 1.nmconnection")
        return

    # Validate static mode input
    if mode == "static" and not ip:
        print("Error: Static mode requires an IP address.")
        return

    # Get default gateway
    gateway = subprocess.check_output("ip route show default | awk '/default/ {print $3}'", shell=True).decode().strip()

    # Backup file
    backup_file(file_path)

    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    in_ipv4 = False

    # Process each line
    for line in lines:
        stripped = line.strip()

        # Check for start of [ipv4] section
        if stripped == "[ipv4]":
            in_ipv4 = True
            new_lines.append(line)
            if mode == "static" and ip and not any("address1=" in l for l in new_lines):
                new_lines.append("method=manual\n")
                new_lines.append(f"address1={ip}/{subnet},{gateway}\n")
                new_lines.append("dns=8.8.8.8;1.1.1.1\n")
            continue

        elif stripped.startswith("[") and stripped != "[ipv4]":
            in_ipv4 = False

        # Modify [ipv4] settings
        if in_ipv4:
            if stripped.startswith("method="):
                if mode == "dhcp":
                    new_lines.append("method=auto\n")
                else:
                    new_lines.append("method=manual\n")

            elif stripped.startswith("address1="):
                if mode == "static" and ip:
                    new_lines.append(f"address1={ip}/{subnet},{gateway}\n")
                elif mode == "dhcp":
                    continue
                else:
                    new_lines.append(line)

            elif stripped.startswith("dns="):
                if mode == "static":
                    new_lines.append("dns=8.8.8.8;1.1.1.1\n")
                elif mode == "dhcp":
                    continue
                else:
                    new_lines.append(line)

            else:
                new_lines.append(line)

        else:
            new_lines.append(line)

    # Write changes
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

    print(f"Network configuration updated to {mode} mode.")


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

    parser_validate.add_argument("--ip", required=True, help="Requires an IP address to validate")
    parser_validate.add_argument("-s","--subnet", required=True, help="Requires a subnet to validate")

    # Subcommand: backup
    parser_backup = subparsers.add_parser("backup", help="Backup a network config file")
    parser_backup.add_argument("-f","--file", required=True, help="Path to the file to back up")

    # Subcommand: restore 
    parser_restore = subparsers.add_parser("restore", help="Restore configuration from a backup")

    # Subcommand: change
    parser_change = subparsers.add_parser("change", help="Change network mode (static/dhcp)")
    parser_change.add_argument("-f","--file", nargs='?', default="/etc/NetworkManager/system-connections/Wired connection 1.nmconnection", help="Path to the config file")
    parser_change.add_argument("-m","--mode", choices=["static", "dhcp"], required=True, help="Network mode to set")
    parser_change.add_argument("--ip", help="Static IP address (required for static mode)")
    parser_change.add_argument("-s","--subnet", help="Missing Subnet (required for static mode)")


    # Subcommand: ping
    parser_ping = subparsers.add_parser("ping", help="Ping a target to test connectivity")
    parser_ping.add_argument("--target", default="8.8.8.8", help="Target IP to ping")

    args = parser.parse_args()


    # Save path for restoring
    orig_path = "/etc/NetworkManager/system-connections/Wired connection 1.nmconnection"
    backup_path = orig_path + '.bak'

    if args.command == "validate":
        validate_ip(args.ip, args.subnet)

    elif args.command == "backup":
        try:
            backup_file(args.file)
        except FileNotFoundError as e:
            print(f"ERROR: {e}")

    elif args.command == "restore":
        try:
            if os.path.exists(orig_path):
                os.remove(orig_path)
            shutil.copy2(backup_path, orig_path)
            print("Restored configuration from backup file")
            # Removes the runtime configuration so it loads the new one
            if os.path.exists('/run/NetworkManager/system-connections/Wired connection 1.nmconnection'):
                os.remove('/run/NetworkManager/system-connections/Wired connection 1.nmconnection')
                flush = subprocess.run(["sudo", "ip", "addr", "flush", "dev", "ens33"])
                res = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                if flush.returncode != 0 or res.returncode != 0:
                    print("ERROR: Could not apply changes.")
                else:
                    print("New network configuration successfully updated.")

        except FileNotFoundError:
            print('ERROR: No backup file found')  

    elif args.command == "change":
        if args.mode == "static":
            if not args.ip:
                print("ERROR: Static requires an IP address. Use --ip followed by the IP address")
                return
            if not validate_ip(args.ip, args.subnet):
                print("ERROR: Invalid or missing IP and subnet.")
                return
        change_network_mode(args.file, args.mode, ip=args.ip, subnet=args.subnet)
        # Restart NetworkManager to apply changes
        print("Restarting NetworkManager to apply new changes")
        # Removes the runtime configuration so it loads the new one
        if os.path.exists('/run/NetworkManager/system-connections/Wired connection 1.nmconnection'):
            os.remove('/run/NetworkManager/system-connections/Wired connection 1.nmconnection')
        flush = subprocess.run(["sudo", "ip", "addr", "flush", "dev", "ens33"])
        res = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
        if flush.returncode != 0 or res.returncode != 0:
             print("ERROR: Could not apply changes.")
        else:
             print("New network configuration successfully updated.")

    elif args.command == "ping":
        if not test_ping(args.target):
            print("Ping failed: there may be an issue with the current network configuration.")
            # Attempt to restore NetworkManager config from backup
            
            restore = input('\nWould you like to restore from backup? (y/n): ')
            if restore == 'y':
                if os.path.isfile(backup_path):
                    try:
                        if os.path.isfile(orig_path):
                            os.remove(orig_path)
                            print(f"Deleted current config at {orig_path}.")
                        shutil.copy2(backup_path, orig_path)
                        print(f"Restored backup configuration from {backup_path} to {orig_path}.")
                        # Restart to apply restored config
                        print("Restarting NetworkManager to apply new changes.")
                        # Removes the runtime configuration so it loads the new one
                        if os.path.exists('/run/NetworkManager/system-connections/Wired connection 1.nmconnection'):
                            os.remove('/run/NetworkManager/system-connections/Wired connection 1.nmconnection')
                        flush = subprocess.run(["sudo", "ip", "addr", "flush", "dev", "ens33"])
                        res = subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
                        if flush.returncode != 0 or res.returncode != 0:
                            print("ERROR: Could not apply changes.")
                        else:
                            print("New network configuration successfully updated.")

                    except PermissionError:
                        print("ERROR: Could not restore backup. Try running with elevated privileges.")
                    except OSError as e:
                        print(f"ERROR: Failed to restore backup: {e}")
            else:
                exit()
    else:
        parser.print_help()


# ----------------------------
# Entry Point
# ----------------------------
if __name__ == "__main__":
    main()
