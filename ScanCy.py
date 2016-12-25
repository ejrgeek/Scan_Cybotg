#coding: utf-8

import socket

ip=input("IP/HOST ou URL > ")
portas=[]
x=int(input("Total de portas > "))
aux=0


while aux<x:
    portas.append(int(input("Porta > ")))
    aux+=1
for porta in portas:
    cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    conexao=cliente.connect_ex((ip,porta))
    if conexao == 0:
        print (porta," > Porta Aberta")
    else:
        print (porta," > Porta Fechada")
# 69 992372089