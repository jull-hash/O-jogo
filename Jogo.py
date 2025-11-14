import redis
import os
import time
import random

r = redis.Redis(host="10.1.69.95",port=6379, db=0)
r.ping()


salaDesejada = ""
sala = ""
player2 = 0
player1 = 0
jgp1 = ""
jgp2 = ""
continuamenu= True



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print("\nJJJOGO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n!!!!!!!JJJOGO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n\n!!!!!!!!!!!!!!JJJOGO!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n\n\n!!!!!!!!!!!!!!!!!!!!!JJJOGO!!!!!!!!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!JJJOGO!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!JJJOGO!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!OGOJJJ")
time.sleep(0.5)
limpar_tela()
print("\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!OGOJJJ!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n\n\n!!!!!!!!!!!!!!!!!!!!!OGOJJJ!!!!!!!!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n\n!!!!!!!!!!!!!!OGOJJJ!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\n\n!!!!!!!OGOJJJ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()
print("\nOGOJJJ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.5)
limpar_tela()

           
while continuamenu==True:
    limpar_tela()
    entrada = (input("\nDeseja criar uma sala ou entrar em uma sala?\n1- Criar uma sala\n2- Entrar em uma sala existente\nR:"))
    if entrada == '1':
        continuamenu=False
        limpar_tela()
        while True:


            sala = input("\nNome da sala\nR:")


            if sala!= "":
                player1 =+ 1
                break
       
    elif entrada == '2':
        continuamenu=False
        limpar_tela()
        while True:
            print("OBS:\nAo tentar entrar na sala, se acontecer de não reconhecer o 'p1'\né provável que a sala não exista.")
            sala = (input("\nDigite o número da sala que você vai entrar\nR:"))


            if sala != "":
                player2 =+ 1
                break
    else:
        limpar_tela()
        print("\nOpção não disponível\n")
        time.sleep(2)
        continuamenu=True


if player1 == 1:
    continua=True
    while continua==True:
        limpar_tela()
        jgp1 = input("\nFaça sua jogada \n(apenas números)\nR:")
        

        if (jgp1.isalpha()):
            limpar_tela()
            print("\n 🔴 Valor inválido 🔴\n")
            time.sleep(2)
            continua=True


        elif jgp1 != "":
            limpar_tela()
            aguardandocontinua=True
            continua= False
            r.hset(sala,"p1",jgp1)
            r.hset(sala,"p2","")

            while aguardandocontinua == True:
                print("\nAguardando jogada do player 2...🕝")
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 2...🕑")
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 2...🕜")
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 2...🕐") 
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 2...🕧")
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 2...🕛")    
                time.sleep(0.5)
                limpar_tela()

            while True:
                dados = r.hgetall(sala)
                p1 = dados["p1".encode()].decode()
                p2 = dados["p2".encode()].decode()
                if p1 != "" and p2 != "":
                    aguardandocontinua= False
                    for i in range(1,20):
                        num1 = random.randint(1, 100)
                        num2 = random.randint(1, 100)
                        limpar_tela()
                        print (f"\n     |{num1}  ⚔️   {num2}|\n")
                        time.sleep(0.09)
                    limpar_tela()
                    p1int = int(p1)
                    pl2int = int(p2)
                    limpar_tela()
                    if p1int > pl2int:
                        print("P1 venceu!")
                        print(p1int,">",pl2int)
                        r.delete(sala,"p1",jgp1)
                        r.delete(sala,"p2",jgp2)
                    elif pl2int > p1int:
                        print("p2 venceu!")
                        print(p1int,"<",pl2int)
                        r.delete(sala,"p1",jgp1)
                        r.delete(sala,"p2",jgp2)
                    elif p1int == pl2int:
                        print("EMPATE!")
                        print(f"!!{p1int} = {pl2int}!!")
                        r.delete(sala,"p1",jgp1)
                        r.delete(sala,"p2",jgp2)
                    break
           


elif player2 == 1:
    continua=True
    while continua==True:
        limpar_tela()
        jgp2 = input("\nFaça sua jogada\nR:")
        if (jgp2.isalpha()):
            limpar_tela()
            print("\nvalor inválido\n")
            time.sleep(2)
            continua=True


        elif jgp2 != "":
            aguardandocontinua= True
            limpar_tela()
            continua= False
            r.hset(sala,"p2",jgp2)

            while aguardandocontinua == True:
                print("\nAguardando jogada do player 1...🕝")
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 1...🕑")
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 1...🕜")
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 1...🕐") 
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 1...🕧")
                time.sleep(0.5)
                limpar_tela()
                print("\nAguardando jogada do player 1...🕛")    
                time.sleep(0.5)
                limpar_tela()

            while True:
                dados = r.hgetall(sala)
                p1 = dados["p1".encode()].decode()
                p2 = dados["p2".encode()].decode()
                if p1 != "" and p2 != "":
                    aguardandocontinua = False
                    for i in range(1,20):
                        num1 = random.randint(1, 100)
                        num2 = random.randint(1, 100)
                        limpar_tela()
                        print (f"\n     |{num1}  ⚔️   {num2}|\n")
                        time.sleep(0.09)
                    limpar_tela()
                    p1int = int(p1)
                    pl2int = int(p2)
                    limpar_tela()
                    if p1int > pl2int:
                        print("P1 venceu!")
                        print(p1int,">",pl2int)
                        r.delete(sala,"p1",jgp1)
                        r.delete(sala,"p2",jgp2)
                    elif pl2int > p1int:
                        print("p2 venceu!")
                        print(p1int,"<",pl2int)
                        r.delete(sala,"p1",jgp1)
                        r.delete(sala,"p2",jgp2)
                    elif p1int == pl2int:
                        print("EMPATE!")
                        print(f"!!{p1int} = {pl2int}!!")
                        r.delete(sala,"p1",jgp1)
                        r.delete(sala,"p2",jgp2)
                    break
           
