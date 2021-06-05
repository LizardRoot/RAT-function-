import os

try:
	os.system('netsh advfirewall set allprofiles state off')
except Exception as e:
	print(e)
