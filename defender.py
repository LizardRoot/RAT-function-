# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinDefend
# Дважды кликните мышью по параметру Start в правой панели редактора реестра и задайте для него значение 4. 
# reboot

import winreg

winreg.CreateKey(key, sub_key)