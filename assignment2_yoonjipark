# I was not able to push to this repo, so i forked the repo and created my own repo. this is the last edition I pushed in my repo so far 

#!/usr/bin/env python3
# Author : Yoonji Park
# change_network_mode function


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
