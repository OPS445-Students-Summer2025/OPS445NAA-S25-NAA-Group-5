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
<<<<<<< Updated upstream
    # TODO: Use shutil to copy the file safely
    pass

=======
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
>>>>>>> Stashed changes

# ----------------------------
# Function 3: Change Network Mode (static/dhcp)
# ----------------------------
def change_network_mode(file_path, mode, ip=None):
    """
    Changes the network mode to either static or dhcp.

<<<<<<< Updated upstream
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
=======
        # Check if the file exists
        if not os.path.exists(file_path):
                print(f"Error: File {file_path} does not exist.")
                return False

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
                                    new_lines.append("dns=8.8.8.8.8;\n")
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
>>>>>>> Stashed changes


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
<<<<<<< Updated upstream
    # TODO: Use subprocess to run 'ping -c 2 <target>' and print result
    pass
=======
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
>>>>>>> Stashed changes


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
        flush = subprocess.run(["sudo", "ip", "addr", "flush", "dev", "ens33"])
        down = subprocess.run(["sudo", "nmcli", "connection", "down", "'Wired Connection 1'"])
        up = subprocess.run(["sudo", "nmcli", "connection", "up", "'Wired Connection 1'"])

    elif args.command == "ping":
        if not test_ping(args.target):
            print("Ping failed: there may be an issue with the current network configuration.")
            # Attempt to restore NetworkManager config from backup
            orig_path = "/etc/NetworkManager/system-connections/'Wired Connection 1.nmconnection"
            backup_path = orig_path + '.bak'
            if os.path.isfile(backup_path):
                try:
                    if os.path.isfile(orig_path):
                        os.remove(orig_path)
                        print(f"Deleted current config at {orig_path}.")
                    shutil.copy2(backup_path, orig_path)
                    print(f"Restored backup configuration from {backup_path} to {orig_path}.")
                    # Restart to apply restored config
                    print("Restarting NetworkManager to apply new changes.")
                    
                    flush = subprocess.run(["sudo", "ip", "addr", "flush", "dev", "ens33"])
                    down = subprocess.run(["sudo", "nmcli", "connection", "down", "'Wired Connection 1'"])
                    up = subprocess.run(["sudo", "nmcli", "connection", "up", "'Wired Connection 1'"])
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
