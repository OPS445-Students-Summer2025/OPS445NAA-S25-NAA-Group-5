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



