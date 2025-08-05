# 📡 Assignment 2 - Network Configuration Tool

This command-line tool helps manage and troubleshoot network settings using **Netnetwork_configuration_tool.py**.

---

## ✅ Features

- Validate an IPv4 address
- Backup a network configuration file
- Change network mode (static or DHCP)
- Test network connectivity using ping
- Automatically restore backup if ping fails

---

## 🧰 Requirements

- Python **3.6+**
- Linux system (for NetworkManager operations)
- Run with **sudo** for system-level changes

---

## 🔧 Setup

This will download your **Network_configuration_tool.py** locally, allowing you to use them on your command prompt.

### 1. Clone your repository into your console using SSH:

```bash
git clone <ssh link> ~/NetworkConftools/
```

--- 

## 🖥️ Usage

```bash
python network_configuration_tool.py <command> [options]
```

---

## 📋 Available Commands and Parameters

| Command    | Parameters                                      | Required | Description                                 |
|------------|-------------------------------------------------|----------|---------------------------------------------|
| `validate` | `<ip>`                                          | ✅       | Validates if the given IP is a proper IPv4  |
| `backup`   | `<file_path>`                                   | ✅       | Creates a backup of the given config file   |
| `change`   | `<file_path>` `<mode: static|dhcp>` `--ip <ip>` | ✅       | Changes network mode (static or dhcp)       |
| `ping`     | `--target <ip>`                                 | ❌       | Pings the IP |

---

## Guide to run Commands 

### ✅ Validate IP Address

```bash
python network_configuration_tool.py validate <YOUR-IP-ADDRESS>
```

### 🛟 Backup Config File

```bash
python network_configuration_tool.py backup /etc/NetworkManager/NetworkManager.conf
```

### 🔁 Change Network Mode

**Switch to DHCP:**
```bash
python network_configuration_tool.py change /etc/NetworkManager/NetworkManager.conf dhcp
```

**Switch to Static IP:**
```bash
python network_configuration_tool.py change /etc/NetworkManager/NetworkManager.conf static --ip <YOUR-IP-ADDRESS>
```

### 📶 Test Network Connectivity

```bash
python network_configuration_tool.py ping --target <YOUR-IP-ADDRESS>
```

> If ping fails, the script attempts to restore the previous config from backup.

---

## ⚠️ Notes

- Use **sudo** for commands that modify system files or restart services.
- Backup files are stored in: `~/backups/`
- The script restarts `NetworkManager` after changes.

---
