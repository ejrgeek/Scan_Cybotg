#coding: utf-8
    
import socket
import time

print("""\033[1;31m
  ██████  ▄████▄   ▄▄▄       ███▄    █  ▄████▄  ▓██   ██▓
▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ ▒██▀ ▀█   ▒██  ██▒
░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄   ▒██ ██░
  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒  ░ ▐██▓░
▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░  ░ ██▒▓░
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░   ██▒▒▒ 
░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒    ▓██ ░▒░ 
░  ░  ░  ░          ░   ▒      ░   ░ ░ ░         ▒ ▒ ░░  
      ░  ░ ░            ░  ░         ░ ░ ░       ░ ░     
         ░                             ░         ░ ░     
Coder > ejr_geek
GitHub > github.com/ejrgeek | ScanFullCy v2.0
\033[0;0m""")
ip=input("\033[1;34mIP/HOST ou URL > \033[0;0m")

for porta in range(0,65536):
    cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    conexao=cliente.connect_ex((ip,porta))
    if conexao == 0:
        print ("\033[1;32m[☢]",porta,"> Porta Aberta\033[0;0m")
        time.sleep(0.2)
    else:
        print ("\033[1;31m",porta,"> Porta Fechada\033[0;0m")
