#imports
import os
import time



# variaveis globais
listagem_deposito = []
listagem_saque = []
listagem_completa = []
saldo = deposito =  saque = cont = 0 

clear = lambda: os.system('cls')


def op_inicial():
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
    
def op_extrato():
    if cont > 1:
        clear()
        
    print("""
        Sistema bancário GX
         ______________________   
        |    Operações de      |
        |      Extrato:        |
        |                      |
        |   1- Deposito        |
        |   2- Saque           |
        |   3- Completa        |
        |   4- Sair            |
        |______________________|
    """)

def loading(text):
    clear()
    mensagem_deposito = text+"."
    print(mensagem_deposito)
    time.sleep(0.5)
    clear()
    print(mensagem_deposito+".")
    time.sleep(0.5)
    clear()
    print(mensagem_deposito+"..")
    time.sleep(0.5)

def sacar(saque, saldo):
    while True:
            try:
                saque = int(input("Informe o valor de saque: "))
            except ValueError:
                print("... Value Error")

            if saque <=1:
                loading("Verificando Saque")
                print("valor de saque é nulo, negativo ou texto, tente novamente...")
                continue
            elif saque > saldo:
                loading("Verificando Saque")
                print("Valor de saque é maior que o saldo atual ou é um texto! Tente novamente.")
            else:
                loading("Verificando Saque")
                return saque

def depositar(deposito):
    while True:
            try:
                deposito = int(input("Informe o valor de deposito: "))
            except ValueError:
                print("... Value Error")

            if deposito <=1:
                loading("Depositando")
                print("valor depositado é nulo, negativo ou texto, tente novamente...")
                continue
            else:
                loading("Depositando")
                return deposito

while True:
    op_inicial() 

    esc = int(input("Escolha uma operação: "))
    if esc == 1:
        
        novo_deposito = depositar(deposito)
        print(f"valor depositado Com sucesso")
        listagem_deposito.append(novo_deposito)
        listagem_completa.append(novo_deposito)
        saldo += novo_deposito
        time.sleep(2)
        clear()
        continue

    elif esc == 2:
        novo_saque = sacar(saque, saldo)
        print(f"valor sacado Com sucesso")
        listagem_saque.append(novo_saque)
        listagem_completa.append(-novo_saque)
        saldo -= novo_saque
        time.sleep(2)
        clear()
        continue

    elif esc == 3:
        while True:
            clear()
            op_extrato()
            esc_extrato = int(input("Informe uma modalidade de extrato: "))
            match esc_extrato:
                case 1:
                    for d in listagem_deposito:
                        print(f"Depositado:{d}")
                    time.sleep(4)
                        
                case 2:
                    for s in listagem_saque:
                        print(f"Sacado: {s}")
                    time.sleep(4)
                case 3:
                    for i in listagem_completa:
                        if i > 0:
                            print(f"Deposito: {i}")
                        elif i < 0:
                            print(f"Sacado: {i}")
                        else:
                            print("erro!")
                    time.sleep(4)
                case 4:
                    break

                case _:
                    print("erro, tente novamente:")
                    continue
                                             
    elif esc == 4:
        clear()
        print(f"{" "*40}Saldo da conta: {saldo}")
        time.sleep(3)
    
    elif esc == 5:
        clear()
        print(f"{" "*40}Obrigado pela confiança!")
        time.sleep(2)
        break
    
    cont+=1