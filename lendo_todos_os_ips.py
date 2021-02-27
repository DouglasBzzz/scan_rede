import os
import subprocess

os.system("clear")
ip = input("ip inicial (192.168.2.1); ").split(".")
print("testando...")
for i in range(1,101):
    ip[3] = str(i)
    ip_formatado = ".".join(ip)
    rs = os.system(f"ping -c 1 {ip_formatado}")
    if rs == 0:
        print(f"o {ip_formatado} está online")
        subprocess.Popen(["say", "O telefone do Douglas está online"])
        break
