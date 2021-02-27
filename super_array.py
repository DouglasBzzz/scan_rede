import re, os

ips = "192.168.2."

os.system("clear")

#print("+-----------------+")
print("+-----------------+")

print("[+] verificando ips na rede [+]")

for i in range(100,255):
    num = str(i)
    cmd = "ping -t "+ips+num
    r = "".join(os.popen(cmd).readlines())
    if re.search("1 received", r):
        print("[+] Host on: ", ips+num)