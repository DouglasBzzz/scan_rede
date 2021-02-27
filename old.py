import subprocess

for ping in range(0,255):
    endereco = "127.0.0."+str(ping)
    res = subprocess.call(["ping", "-c", "1", endereco])
    if res == 0:
        print("ping to ", endereco, " Ok")
    elif res == 2:
        print("sem resposta do endereco ", endereco)
    else:
        print("ping no ", endereco, " falhou")