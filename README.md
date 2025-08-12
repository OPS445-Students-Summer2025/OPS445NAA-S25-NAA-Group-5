# 📡 Assignment 2 - Network Configuration Tool

This command-line tool helps manage and troubleshoot network settings using **assignment2.py**.

---

## ✅ Features

- Validate an IPv4 address
- Backup a network configuration file
- Change network mode (static or DHCP)
- Test network connectivity using ping
- Automatically restore backup if ping fails

---

## 🧰 Requirements

- Python3 **3.6+**
- Linux system (for NetworkManager operations)
- Run with **sudo** for system-level changes

---

## 🔧 Setup

This will download your **assignment2.py** locally, allowing you to use them on your command prompt.

### 1. Clone your repository into your console using SSH:

```bash
git clone <ssh link> ~/NetworkConftools/
```

--- 

## 🖥️ Usage

```bash
python3 assignment2.py <command> [options]
```

---

| **Command** | **Parameters**                                                                                                 | **Required** | **Description**                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| `validate`  | `--ip <ip>`<br>`-s, --subnet <subnet>`                                                                         | ✅            | Validates if the given IP is a proper IPv4.                                                           |
| `backup`    | `-f, --file <file_path>`                                                                                       | ✅            | Creates a backup of the given config file.                                                            |
| `change`    | `-f, --file <file_path>`<br>`-m, --mode <mode: static/dhcp>`<br>`--ip`, `--subnet` (required if mode = static) | ✅            | Changes network settings based on mode. If mode is `static`, `--ip` and `--subnet` are also required. |
| `ping`      | `--target <ip>`                                                                                                | ❌            | Pings the IP address provided.                                                                        |


---

## Guide to run Commands 

### ✅ Validate IP Address

```bash
python3 assignment2.py validate --ip <YOUR-IP-ADDRESS> -s <SUBNET>
```

### 🛟 Backup Config File

```bash
python3 assignment2.py backup -f "/etc/NetworkManager/system-connections/'Wired connection 1.nmconnection'"
```

### 🔁 Change Network Mode

**Switch to DHCP:**
```bash
python3 assignment2.py change /etc/NetworkManager/NetworkManager.conf dhcp
```

**Switch to Static IP:**
```bash
python3 assignment2.py change /etc/NetworkManager/NetworkManager.conf static --ip <YOUR-IP-ADDRESS>
```

### 📶 Test Network Connectivity

```bash
python3 assignment2.py ping --target <YOUR-IP-ADDRESS>
```

> If ping fails, the script attempts to restore the previous config from backup.

---

## ⚠️ Notes

- Use **sudo** for commands that modify system files or restart services.
- Backup files are stored in: `/etc/NetworkManager/system-connections/`
- The script restarts `NetworkManager` after changes.

## References
- Argparse: https://docs.python.org/3/library/argparse.html
---
- Validate an IP : https://www.geeksforgeeks.org/python/python-program-to-validate-an-ip-address
