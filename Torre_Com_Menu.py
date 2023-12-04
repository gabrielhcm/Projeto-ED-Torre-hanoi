import sys
import time

#trasformar a pilha em uma lista, talvez sirva pra algo no futuro.

auxiliar1 = []
auxiliar2 = []
auxiliar3 = []


#Armazenas o elemento que foi feito o pop, assim transnformando ele no disco que está fora das torres 

valorremovido = int()
popescolhidot = int()
popemint = popescolhidot
popescolhido = []
popescolhidoint = list(map(int,popescolhido))

#popescolhidoconvertido = list(map(int,popescolhido))

#popvalor = int()



topo1 = int()
topoemint1 = topo1
topo2 = int()
topoemint2 = topo2
topo3 = int()
topoemint3 = topo3

class Noh1:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada1:
    def __init__(self):
        self.cabeca = None
    
    def isEmpty(self):
        return self.cabeca is None

    def push(self, valor):
        novo_no = Noh1(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def pop(self):
        if self.isEmpty():
            return None
        removido = self.cabeca
        popescolhidot = removido.valor
        popescolhido.append(popescolhidot)
        #popescolhido.append(popescolhidot)
        #discom = popescolhido[0]
        self.cabeca = self.cabeca.proximo
        return removido.valor , popescolhido
    def peek(self):
        if self.isEmpty():
            return None
        topo1.append(self.cabeca.valor)    
        return self.cabeca.valor ,topo1    
    def printpilha(self):
        current = self.cabeca
        while current:
            auxiliar1.append(current.valor)
            print(current.valor, end=' ')
            current = current.proximo


class Noh2:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada2:
    def __init__(self):
        self.cabeca = None
    
    def isEmpty(self):
        return self.cabeca is None

    def push(self, valor):
        novo_no = Noh2(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def pop(self):
        if self.isEmpty():
            return None
        removido = self.cabeca
        popescolhidot = removido.valor
        popescolhido.append(popescolhidot)
        self.cabeca = self.cabeca.proximo
        return removido.valor , popescolhido
    def peek(self):
        if self.isEmpty():
            return None
        topo2.append(self.cabeca.valor)    
        return self.cabeca.valor ,topo2
    def printpilha2(self):
        current = self.cabeca
        while current:
            auxiliar2.append(current.valor)
            print(current.valor, end='  ')
            current = current.proximo
class Noh3:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
class PilhaEncadeada3:
    def __init__(self):
        self.cabeca = None
    
    def isEmpty(self):
        return self.cabeca is None

    def push(self, valor):
        novo_no = Noh3(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def pop(self):
        if self.isEmpty():
            return None
        removido = self.cabeca
        popescolhidot = removido.valor
        popescolhido.append(popescolhidot)
        self.cabeca = self.cabeca.proximo
        return removido.valor , popescolhido
    def peek(self):
        if self.isEmpty():
            return None
        topo3.append(self.cabeca.valor)    
        return self.cabeca.valor ,topo3
    def printpilha3(self):
        current = self.cabeca
        while current:
            auxiliar3.append(current.valor)
            print(current.valor, end=' \n ')
            current = current.proximo 


#colocando os discos na torre 

PilhaEncadeada1 = PilhaEncadeada1()
PilhaEncadeada1.push(10)
PilhaEncadeada1.push(8)
PilhaEncadeada1.push(6)
PilhaEncadeada2 = PilhaEncadeada2()
#PilhaEncadeada2.push(11)
#PilhaEncadeada3 = PilhaEncadeada3()
#PilhaEncadeada3.push(12)
PilhaEncadeada3 = PilhaEncadeada3()


#Criação do menu com as opçoes!


def menu_principal():
    print("Menu:")
    print("Escolha uma das opçoes:")
    print("0. Regras da torre ")
    print("1. retirar uma peça de lugar")
    print("2. Colocar uma peça em outro disco")
    print("3. Mostrar o disco que você está segurando")
    print("4. Imprimir as torres")
    print("5. Sair")
    #time.sleep(1)

def regras_torre():
    print("Apenas um disco pode ser movido por vez e nunca um disco maior deve ficar por cima de um disco menor.")

def retirar_peca():
    print("Escolha uma torre para remover uma peça!: \n Torre A \n Torre B \n Torre C \n Voltar ao menu principal F ")
#mover = None
    mover = str(input()).upper()
    print(mover)
    if mover == "A":
        print("Removeu:") 
        valorremovidotemp = PilhaEncadeada1.pop()
        #print(popescolhido)
        popint = int(popescolhido[0])
        print(popint)
        poptemp = popint
        print("pilha depois da remoção:")
        PilhaEncadeada1.printpilha()
        return poptemp

        return 
        #break
    elif mover == "B": 
        #print("tente digitar o numero da torresfds!")
         #print("tente digitar o numero da torre!")
        print("Removeu:")
        valorremovidotemp = PilhaEncadeada2.pop()
        popint = int(popescolhido[0])
        print(popint)
        poptemp = popint
        #print(valorremovidotemp) 
        #valorremovido = valorremovidotemp
        print("pilha depois da remoção")
        PilhaEncadeada2.printpilha2()
        return poptemp
    elif mover == "C":   
        #print("tente digitar o numero da torrfdse!")
        print("Removeu:")
        valorremovidotemp = PilhaEncadeada3.pop()
        popint = int(popescolhido[0])
        print(popint)
        poptemp = popint
        #print(valorremovidotemp) 
        valorremovido = valorremovidotemp
        print("pilha depois da remoção")
        PilhaEncadeada3.printpilha3()
        return poptemp
    elif mover == "F":
        return
    #else:
    #print("tente digitar o numero da torre!")
        print("batata")

def colocar_peca():
     
    #escolhatorreremover = True
    #while escolhatorreremover:
    print("Escolha uma torre para colocar uma peça!: \n Torre A \n Torre B \n Torre C \n Voltar ao menu principal F ")
    mover = str()
    mover = str(input()).upper()
    print(mover)
    #popescolhidoint = list(map(int,popescolhido))
    #print (popescolhidoint)  
    if mover == "A":
            PilhaEncadeada1.push(popescolhido[0])
            print(f"Você colocou a peça:{popescolhido}!")
            print(popescolhido)
            popescolhido.clear()
            print(topo1)
            #print("tente digitar o numero da torresfds!")
    elif mover == "B": 
        popescolhidoint = list(map(int,popescolhido))
        print (popescolhidoint)  
        print(topo2)    
        PilhaEncadeada2.push(popescolhido[0])
        print(f"Você colocou a peça:{popescolhido}!")
        print(popescolhido)
        popescolhido.clear()
        
        #if popescolhidoint[0] > topo2:
            #print("Você nao pode colocar uma peça maior que a peça que está no topo da torre!1")
    elif mover == "C":
        popescolhidoint = list(map(int,popescolhido)) 
        print (popescolhidoint)
        print(topo3)  
        PilhaEncadeada3.push(popescolhido[0])
        print(f"Você colocou a peça:{popescolhido}!")
        print(popescolhido)
        popescolhido.clear()
        #print("tente digitar o numero da torresfds!")
        #if popescolhidoint[0] != topoemint3:
          #  print("Você nao pode colocar uma peça maior que a peça que está no topo da torre!2")

    elif mover == "F":
         #break
         print("batata")
    # else:
    #     print("tente digitar o numero da torre!")


def Mostrar_discosegurando():
    
    if popescolhido == None:
        print("Você nao esta com nenhuma peça em mãos")
    else:    
        print(f"Você está segurando a peça de tamanho: {popescolhido}")

def imprimir_torres():
    print("A situação atual das torres é:")
    PilhaEncadeada1.printpilha()
    print("\n") 
    PilhaEncadeada2.printpilha2()
    print("\n")
    PilhaEncadeada3.printpilha3()
    popescolhidoint = list(map(int,popescolhido))
    print(popescolhidoint)
    print(topo1)
    

#chamando o menu principal 

def main():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
           retirar_peca()
        elif opcao == "2":
            colocar_peca()
        elif opcao == "3":
            Mostrar_discosegurando()
        elif opcao == "4":
            imprimir_torres()  
        elif opcao == "5":
            sys.exit()
        elif opcao == "0":
            regras_torre()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
  time.sleep(1)  
  main()




