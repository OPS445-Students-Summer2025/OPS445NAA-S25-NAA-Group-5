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
	method_changed = False
	address_set = False
	dns_set = False

	# Process each line
	for line in lines:
    		stripped = line.strip()




