import socket
from pyfiglet import Figlet
from colorama import init, Fore
from datetime import datetime

#Brand Banner
init(convert=True) 
f = Figlet(font="chunky",)
for col in [Fore.LIGHTCYAN_EX]:
    print(col + f.renderText("CAport"))


#base 
count = 0
open_port = []

# input alamat IP/domain yang akan di scan
domain = input(Fore.WHITE + "masukkan ip/domain target : ")

# translate hostname/domain ke IPv4
target = socket.gethostbyname(domain)
	
print("")

#Banner
print(Fore.WHITE + "-" * 21 + "Scanning" + "-" * 21)
print(Fore.WHITE + "Scanning Target: "+ Fore.LIGHTBLUE_EX + target)
print(Fore.WHITE + "Scanning Time: "+ Fore.LIGHTBLUE_EX  + str(datetime.now()))
print(Fore.WHITE + "-" * 50)

# program
try:

    for port in range(17, 24):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(Fore.WHITE + f"Port {port} :", Fore.GREEN +  "Open")
            open_port.append(port)
            count += 1
        else:
            print(Fore.WHITE + f"Port {port} :",Fore.RED + "Close")
        sock.close()
    print(Fore.WHITE + "Scaning selesai,",Fore.GREEN +  f"{count}", Fore.WHITE + "port terbuka ditemukan")
    print(Fore.WHITE + "Port terbuka: ",Fore.GREEN + f"{open_port}")

except KeyboardInterrupt:
		print(Fore.LIGHTRED_EX + "\n Program dihentikan !!!")
		sock.close()

