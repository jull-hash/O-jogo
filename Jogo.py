import redis
import os
import time
import random

r = redis.Redis(host="localhost",port=6379, db=0)
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


def menu():
    global continuamenu, sala, player1, player2
    while continuamenu==True:
        limpar_tela()
        entrada = (input("\nDeseja criar uma sala ou entrar em uma sala?\n1- Criar uma sala\n2- Entrar em uma sala existente\nR:"))
        if entrada == '1':
            continuamenu=False
            limpar_tela()
            while True:


                sala = input("\nNome da sala\nR:")

                if r.exists(sala):
                    print("\n❌ A sala já existe, tente novamente ❌")
                    continue

                elif sala!= "":
                    player1 += 1
                    main()
                    break
       
        elif entrada == '2':
            continuamenu=False
            limpar_tela()
            while True:
                print("OBS:\nAo tentar entrar na sala, se acontecer de não reconhecer o 'p1'\né provável que a sala não exista.")
                sala = (input("\nDigite o número da sala que você vai entrar\nR:"))


                if sala != "":
                    player2 += 1
                    main()
                    break
        else:
            limpar_tela()
            print("\n❌ Opção inválida ❌\n")
            time.sleep(2)
            continuamenu=True

def main():
    global player1, player2, sala, jogadnv, jogadnvNum, continuamenu

    if player1 == 1:
        continua=True
        while continua==True:
            limpar_tela()
            jgp1 = input("\nFaça sua jogada \n(apenas números)\nR:")
        

            if not jgp1.strip().isdigit():
                limpar_tela()
                print("\n 🔴 Valor inválido 🔴\n")
                time.sleep(2)
                continua=True


            elif jgp1 != "":
                limpar_tela()
            
                continua= False
                r.hset(sala,"p1",jgp1)
                r.hset(sala,"p2","")

                print("\nAguardando jogada do player 2...🕝")

                while True:
                    dados = r.hgetall(sala)
                    p1 = dados["p1".encode()].decode()
                    p2 = dados["p2".encode()].decode()
                    if p1 != "" and p2 != "":
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
                            print(" 🎉 P1 venceu! 🎉")
                            print(p1int,">",pl2int)
                            r.delete(sala)
                            r.delete(sala)
                            
                            
                            continuarrr=True
                            while continuarrr == True:
                                jogadnv = input("\nQuer jogar de novo? 1 - Sim | 2 - Não\nR:")
                                if jogadnv.strip().isdigit():
                                    jogadnvNum = int(jogadnv)
                                    if jogadnvNum  == 1:
                                        player1 = 0
                                        player2 = 0
                                        continuamenu = True
                                        sala = " "
                                        continuarrr == False
                                        menu()
                                    if jogadnvNum == 2:
                                        print("\nObrigado por jogar e volte sempre! :)")
                                        continuarrr == False
                                        break
                                    else:
                                        limpar_tela()
                                        print("\n 🔴 Valor inválido 🔴\n")
                                else:
                                    limpar_tela()
                                    print("\n❌ Valor inválido (apenas números) ❌")
                                    
                                    
                        elif pl2int > p1int:
                            print("🎉 P2 venceu! 🎉")
                            print(p1int,"<",pl2int)
                            r.delete(sala)
                            r.delete(sala)
                            
                            
                            continuarrr=True
                            while continuarrr == True:
                                jogadnv = input("\nQuer jogar de novo? 1 - Sim | 2 - Não\nR:")
                                if jogadnv.strip().isdigit():
                                    jogadnvNum = int(jogadnv)
                                    if jogadnvNum  == 1:
                                        player1 = 0
                                        player2 = 0
                                        continuamenu = True
                                        sala = " "
                                        continuarrr == False
                                        menu()
                                    if jogadnvNum == 2:
                                        print("\nObrigado por jogar e volte sempre! :)")
                                        continuarrr == False
                                        break
                                    else:
                                        limpar_tela()
                                        print("\n 🔴 Valor inválido 🔴\n")
                                else:
                                    limpar_tela()
                                    print("\n❌ Valor inválido (apenas números) ❌")
                                    
                                    
                        elif p1int == pl2int:
                            print(" 😵‍💫 ! EMPATE! 😵‍💫")
                            print(f"!!{p1int} = {pl2int}!!")
                            r.delete(sala)
                            r.delete(sala)                            
                            continuarrr=True
                            while continuarrr == True:
                                jogadnv = input("\nQuer jogar de novo? 1 - Sim | 2 - Não\nR:")
                                if jogadnv.strip().isdigit():
                                    jogadnvNum = int(jogadnv)
                                    if jogadnvNum  == 1:
                                        player1 = 0
                                        player2 = 0
                                        continuamenu = True
                                        sala = " "
                                        continuarrr == False
                                        menu()
                                    if jogadnvNum == 2:
                                        print("\nObrigado por jogar e volte sempre! :)")
                                        continuarrr == False
                                        break
                                    else:
                                        limpar_tela()
                                        print("\n 🔴 Valor inválido 🔴\n")
                                else:
                                    limpar_tela()
                                    print("\n❌ Valor inválido (apenas números) ❌")
                    
                        break
           


    elif player2 == 1:
        continua=True
        while continua==True:
            limpar_tela()
            jgp2 = input("\nFaça sua jogada\nR:")
            if not jgp2.strip().isdigit():
                limpar_tela()
                print("\n 🔴 Valor inválido 🔴\n")
                time.sleep(2)
                continua=True


            elif jgp2 != "":
                limpar_tela()
                continua= False
                r.hset(sala,"p2",jgp2)

                print("\nAguardando jogada do player 2...🕝")
            
                while True:
                    dados = r.hgetall(sala)
                    p1 = dados["p1".encode()].decode()
                    p2 = dados["p2".encode()].decode()
                    if p1 != "" and p2 != "":
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
                            print("🎉  P1 venceu! 🎉")
                            print(p1int,">",pl2int)                  
                            continuarrr=True
                            while continuarrr == True:
                                jogadnv = input("\nQuer jogar de novo? 1 - Sim | 2 - Não\nR:")
                                if jogadnv.strip().isdigit():
                                    jogadnvNum = int(jogadnv)
                                    if jogadnvNum  == 1:
                                        player1 = 0
                                        player2 = 0
                                        continuamenu = True
                                        sala = " "
                                        continuarrr == False
                                        menu()
                                    if jogadnvNum == 2:
                                        print("\nObrigado por jogar e volte sempre! :)")
                                        continuarrr == False
                                        break
                                    else:
                                        limpar_tela()
                                        print("\n 🔴 Valor inválido 🔴\n")
                                else:
                                    limpar_tela()
                                    print("\n❌ Valor inválido (apenas números) ❌")
                                    
                                    
                        elif pl2int > p1int:
                            print("🎉 P2 venceu! 🎉")
                            print(p1int,"<",pl2int)
                            continuarrr=True
                            while continuarrr == True:
                                jogadnv = input("\nQuer jogar de novo? 1 - Sim | 2 - Não\nR:")
                                if jogadnv.strip().isdigit():
                                    jogadnvNum = int(jogadnv)
                                    if jogadnvNum  == 1:
                                        player1 = 0
                                        player2 = 0
                                        continuamenu = True
                                        sala = " "
                                        continuarrr == False
                                        menu()
                                    if jogadnvNum == 2:
                                        print("\nObrigado por jogar e volte sempre! :)")
                                        continuarrr == False
                                        break
                                    else:
                                        limpar_tela()
                                        print("\n 🔴 Valor inválido 🔴\n")
                                else:
                                    limpar_tela()
                                    print("\n❌ Valor inválido (apenas números) ❌")
                                
                        elif p1int == pl2int:
                            print(" 😵‍💫 !EMPATE! 😵‍💫")
                            print(f"!!{p1int} = {pl2int}!!")
                            
                            continuarrr=True
                            while continuarrr == True:
                                jogadnv = input("Quer jogar de novo? 1 - Sim | 2 - Não")
                                if jogadnv.strip().isdigit():
                                    jogadnvNum = int(jogadnv)
                                    if jogadnvNum  == 1:
                                        player1 = 0
                                        player2 = 0
                                        continuamenu = True
                                        sala = " "
                                        continuarrr == False
                                        menu()
                                    if jogadnvNum == 2:
                                        print("Obrigado por jogar e volte sempre! :)")
                                        continuarrr == False
                                        break
                                else:
                                    print("Valor inválido (apenas números)")
                        break
           
           

limpar_tela()
print("\nJJJOGO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.1)
limpar_tela()
print("\n!!!!!!!JJJOGO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.1)
limpar_tela()
print("\n!!!!!!!!!!!!!!JJJOGO!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.1)
limpar_tela()
print("\n!!!!!!!!!!!!!!!!!!!!!JJJOGO!!!!!!!!!!!!!!!!!")
time.sleep(0.1)
limpar_tela()
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!JJJOGO!!!!!!!!!!")
time.sleep(0.1)
limpar_tela()
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!JJJOGO!!!")
time.sleep(0.1)
limpar_tela()
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!OGOJJJ")
time.sleep(0.1)
limpar_tela()
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!OGOJJJ!!!!!!!!!!")
time.sleep(0.2)
limpar_tela()
print("\n!!!!!!!!!!!!!!!!!!!!!OGOJJJ!!!!!!!!!!!!!!!!!")
time.sleep(0.2)
limpar_tela()
print("\n!!!!!!!!!!!!!!OGOJJJ!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.2)
limpar_tela()
print("\n!!!!!!!OGOJJJ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.2)
limpar_tela()
print("\nOGOJJJ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(0.2)
limpar_tela()

menu()           
    