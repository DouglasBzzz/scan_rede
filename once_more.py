import subprocess

for ping in range(110,10):
    endereco = "192.168.2."+str(ping)
    res = subprocess.call(["ping", "-c", "1", endereco])
    if res == 0:
        print("pingando no: ", endereco, "OK")
        #if (endereco == "192.168.2.111"):
            #subprocess.Popen(["say", "o dispositivo do douglas está na rede"])
    elif res == 2:
        print("No response from: ", endereco)
    else:
        print("ping to: ", endereco, "falhou")