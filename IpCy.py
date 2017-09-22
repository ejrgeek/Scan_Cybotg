from socket import *

def PegaIp(d,e):
	d = gethostbyname(e)
	print("\033[1;31mIP > \033[0;0m",d)

print("""\033[1;34m
██╗██████╗          ██████╗██╗   ██╗
██║██╔══██╗        ██╔════╝╚██╗ ██╔╝
██║██████╔╝        ██║      ╚████╔╝
██║██╔═══╝         ██║       ╚██╔╝
██║██║     ███████╗╚██████╗   ██║
╚═╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝
Coder > ejr_geek
GitHub > github.com/ejrgeek | Ip_Cy v3.0
\033[0;0m""")
dominio = input("\033[1;32mURL > \033[0;0m")
PegaIp(dominio, dominio)
