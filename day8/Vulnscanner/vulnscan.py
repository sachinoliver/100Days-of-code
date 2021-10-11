import portscanner

targets_ip = input('[+] * Enter Target to scan for Vulnerable Open Ports: ')
port_number = int(input('[+] * Enter Amount of Ports You Need To Scan(500 - first 500 ports):')
vul_file = input('[+] * Enter Pathe To The File With Vulnerable Softwares: ')
print('\n')

portscanner.scan(targets_ip)
