# Launching ROS Nodes at Start-up in Linux

## Three Methods

### ~/.config/autostart
1. Create/Move python file to root folder (`mv /path/to/file.py /bin`)
2. Navigate to the ~/.config/autostart directory (`cd ~/.config/autostart`)
3. Create a .desktop file (`touch <file name>.desktop`)
4. Make .desktop file executable (`sudo chmod +x <file name>.desktop`)
5. Copy and paste the following code into the .desktop file 
  ```
  [Desktop Entry]
  Encoding=UTF-8
  Name=Name of Application
  Exec=gnome-terminal -- python3 path/to/application.py
  Terminal=true
  Type=Application
  StartupNotify=true
  NoDisplay=true
  ```
6. Reboot system to test the newly created file

**NOTE: Terminal will close when program is finished running.**

[Additional ~/.config/autostart Information](https://askubuntu.com/questions/351582/open-terminal-window-and-execute-python-script-on-startup)

### Systemd service
1. Navigate to systemd directory (`cd etc/systemd/system`)
2. Create a .service file (`touch <file name>.service`)
3. Paste following code into .service file
```
[Unit]
Description=File Name

[Service]
ExecStart=/usr/bin/python3 /path/script.py

[Install]
WantedBy=multi-user.target
```
4. Test service by starting it (`sudo systemctl start <file name>.service`)
5. Enable service to ensure it will run at start-up (`sudo systemctl enable <file name>.service`)
6. Test that it works by rebooting system

**NOTE: This method will NOT open a terminal window**

[Additional Systemd Information](https://unix.stackexchange.com/questions/634410/start-python-script-at-startup)

### Crontab
1. Open the crontab editor (`crontab -e`)
2. Scroll to the bottom of the file, below all the commented code
3. Add a reboot command with the path to your python script (`@reboot python3 /path/to/file.py`)
4. Test that it works by rebooting system

**NOTE: This method will NOT open a terminal window**

[Additional Crontab Information](https://stackoverflow.com/questions/41662821/how-to-run-python-script-at-startup)
