#trasformar a pilha em uma lista, talvez sirva pra algo no futuro.

auxiliar1 = []
auxiliar2 = []
auxiliar3 = []

popescolhidot = None
popescolhido = []



peçasegura = []
topo = []

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
        discom = popescolhido[0]
        self.cabeca = self.cabeca.proximo
        return removido.valor 
        
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
        self.cabeca = self.cabeca.proximo
        return removido.valor
    def peek(self):
        if self.isEmpty():
            return None
        topo.append(self.cabeca.valor)    
        return self.cabeca.valor ,topo
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
        self.cabeca = self.cabeca.proximo
        return removido.valor

    def printpilha3(self):
        current = self.cabeca
        while current:
            auxiliar3.append(current.valor)
            print(current.valor, end=' \n ')
            current = current.proximo 



PilhaEncadeada1 = PilhaEncadeada1()
PilhaEncadeada1.push(2)
PilhaEncadeada1.push(4)
PilhaEncadeada1.push(6)
PilhaEncadeada1.push(8)
PilhaEncadeada1.push(10)
PilhaEncadeada2 = PilhaEncadeada2()
PilhaEncadeada2.push(2)
PilhaEncadeada3 = PilhaEncadeada3()
PilhaEncadeada3.push(2)
rodando = True

peçassegura = None



while rodando:

        print( " Escolha uma das opçoes:\n 0 - Regras da torre \n 1 - retirar uma peça de lugar\n 2 - Colocar uma peça em outro disco\n 3 - mostrar o disco que você está segurando\n 4 - Imprimir as torres\n 5 - Sair ")    
        escolha = ()
        escolha = int(input())
    
        print(escolha)
        
        print(rodando)


        if escolha == 0:
            print("Apenas um disco pode ser movido por vez e nunca um disco maior deve ficar por cima de um disco menor.")

        elif escolha == 1:
                escolhatorre = True
                while escolhatorre:
                    print("Escolha uma torre para remover uma peça!: \n Torre A \n Torre B \n Torre C \n Voltar ao menu principal F ")
                    #mover = None
                    mover = str(input()).upper()
                    print(mover)
                    if mover == "A":
                        print("tente digitar o numero da torre!")
                        print("Removeu:", PilhaEncadeada1.pop())
                        print("pilha depois da remoção")
                        PilhaEncadeada1.printpilha()
                        break
                    elif mover == "B": 
                        print("tente digitar o numero da torresfds!")
                    elif mover == "C":   
                        print("tente digitar o numero da torrfdse!")
                    elif mover == "F":
                         break
                    #else:
                        #print("tente digitar o numero da torre!")    
            
        elif escolha == 2:
                escolhatorreremover = True
                while escolhatorreremover:
                    print("Escolha uma torre para colocar uma peça!: \n Torre A \n Torre B \n Torre C \n Voltar ao menu principal F ")
                    mover = None
                    mover = str(input()).upper()
                    print(mover)
                    if mover == "A":
                        print("tente digitar o numero da torresfds!")
                    elif mover == "B": 
                        print(topo)
                        if (int(popescolhidot)) >= topo:
                            Print("Você nao pode colocar uma peça maior que a peça que está no topo da torre!")
                        else:    
                            PilhaEncadeada2.push(popescolhido[0])
                            print(f"Você colocou a peça:{popescolhido}!")
                            print(popescolhido)
                            popescolhido.clear()
                        
                    elif mover == "C":   
                        print("tente digitar o numero da torrfdse!")
                    elif mover == "F":
                         break
                    #else:
                        #print("tente digitar o numero da torre!") 
        
        elif escolha == 3:
            peçasegura = popescolhido
            print(peçasegura)
            if peçasegura == []:
                    print("Você nao esta com nenhuma peça em mãos")
            else:    
                    print(f"Você está segurando a peça de tamanho: {peçasegura}")
               
        
            
        elif escolha == 4:
                print("tente digitar o numero da torre!")
                PilhaEncadeada1.printpilha()
                print("\n") 
                PilhaEncadeada2.printpilha2()
                print("\n")
                PilhaEncadeada3.printpilha3()
                
                
        elif escolha == 5:
            rodando == False






