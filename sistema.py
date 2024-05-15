#imports
import os
import time



# variaveis globais
listagem_deposito = listagem_saque = []
saldo = deposito =  saque = cont = 0 

clear = lambda: os.system('cls')

def depositando():
    clear()
    mensagem_deposito ="deposintando."
    print(mensagem_deposito)
    time.sleep(1)
    clear()
    print(mensagem_deposito+".")
    time.sleep(1)
    clear()
    print(mensagem_deposito+"..")
    time.sleep(1)
def verificando():
    clear()
    mensagem_deposito ="verificações."
    print(mensagem_deposito)
    time.sleep(0.5)
    clear()
    print(mensagem_deposito+".")
    time.sleep(0.5)
    clear()
    print(mensagem_deposito+"..")
    time.sleep(0.5)

while True:
    if cont > 1:
        clear()
        
    print("""
        Sistema bancário GX
         ______________________   
        |   Operações:         |
        |                      |
        |   1- Deposito        |
        |   2- Saque           |
        |   3- Extrato         |
        |   4- saldo           |
        |   5- Sair            |
        |______________________|
    """)
    esc = int(input("Escolha uma operação: "))



    if esc == 1:
        while True:
            try:
                deposito = int(input("Informe o valor de deposito: "))
            except ValueError:
                print("... Value Error")

            if deposito <=1:
                depositando()
                print("valor depositado é nulo, negativo ou texto, tente novamente...")
                continue
            else:
                depositando()
                print(f"valor depositado Com sucesso")
                listagem_deposito.append(deposito)
                saldo += deposito
                time.sleep(2)
                clear()
                break
    if esc == 2:
        while True:
            try:
                saque = int(input("Informe o valor de saque: "))
            except ValueError:
                print("... Value Error")

            if saque <=1:
                verificando()
                print("valor de saque é nulo, negativo ou texto, tente novamente...")
                continue
            elif saque > saldo:
                verificando()
                print("Valor de saque é maior que o saldo atual ou é um texto! Tente novamente.")
            else:
                verificando()
                print(f"valor sacado Com sucesso")
                listagem_saque.append(saque)
                saldo -= saque
                time.sleep(2)
                clear()
                break
                
    if esc == 4:
        clear()
        print(f"{" "*40}Saldo da conta: {saldo}")
        time.sleep(3)
    if esc == 5:
        clear()
        print(f"{" "*40}Obrigado pela confiança!")
        time.sleep(2)
        break
    cont+=1