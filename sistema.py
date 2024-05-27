#imports
import os
import time



# variaveis globais
listagem_deposito = []
listagem_saque = []
listagem_completa = []
saldo = 0
deposito =  saque = cont = 0 

#limpar prompt
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
    cont=0
    while True:
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
        cont+=1        

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
                saque = int(input("Informe o valor de saque ou 0 para cancelar operação:"))
            except ValueError:
                print("... Value Error")
            
            if saque == 0:
                loading("Cancelando Operação")
                print(f"valor sacado Com sucesso")
                return 0

            elif saque <=0:
                loading("Verificando Saque")
                print("valor de saque é negativo ou texto, tente novamente...")
                continue
            
            elif saque > saldo:
                loading("Verificando Saque")
                print("Valor de saque é maior que o saldo atual ou é um texto! Tente novamente.")
            else:
                loading("Verificando Saque")
                listagem_saque.append(saque)
                listagem_completa.append(-saque)
                
                return saque

def depositar(dep = deposito):
    while True:
            try:
                dep = int(input("Informe o valor de deposito ou 0 para cancelar operação: "))
            except ValueError:
                print("... Value Error")
            
            if dep == 0:
                loading("Cancelando Operação")
                return 0
            elif dep<=1:
                loading("Depositando")
                print("valor depositado é negativo ou texto, tente novamente...")
                continue
            else:
                loading("Depositando")
                listagem_deposito.append(dep)
                listagem_completa.append(dep)
                print(f"valor depositado Com sucesso")
                return dep

while True:
    op_inicial() 

    esc = int(input("Escolha uma operação: "))
    if esc == 1:
        
        novo_deposito = depositar(deposito)
        saldo += novo_deposito
        time.sleep(2)
        clear()
        continue

    elif esc == 2:
        novo_saque = sacar(saque, saldo)
        saldo -= novo_saque
        time.sleep(2)
        clear()
        continue

    elif esc == 3:
            op_extrato()
           
                                             
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