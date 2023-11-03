class Noh1:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada1:
    def __init__(self):
        self.cabeca = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the stack
    def peek(self):
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.cabeca.proximo.valor
    def push(self, valor):
        novo_no = Noh1(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.size += 1

    def pop(self):
        removido = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        self.size -= 1
        return removido


class Noh2:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada2:
    def __init__(self):
        self.cabeca = None

    def push(self, valor):
        novo_no = Noh2(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def pop(self):
        removido = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        return removido
class Noh3:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
class PilhaEncadeada3:
    def __init__(self):
        self.cabeca = None

    def push(self, valor):
        novo_no = Noh3(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def pop(self):
        removido = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        return removido    



'''

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
                    print("Escolha uma torre para remover uma peça!: \n Torre A \n Torre B \n Torre C  \n Torre D \n Voltar ao menu principal F ")
                    mover = None
                    mover = str(input()).upper()
                    print(mover)
                    if mover == "A":
                        print("tente digitar o numero da torre!")

                    elif mover == "B": 
                        print("tente digitar o numero da torresfds!")
                    elif mover == "C":   
                        print("tente digitar o numero da torrfdse!")
                    elif mover == "D":       
                        print("tente digitar o numero da torrfdse!")
                    elif mover == "F":
                         break
                    #else:
                        #print("tente digitar o numero da torre!")    
            
        elif escolha == 2:
                print("tente digitar o numero da torre!")


        
        elif escolha == 3:
                print(f"Você está segurando a peça de tamanho {Peçasegura}")


                if peçassegura == ():
                    print("Você nao esta com nenhuma peça em mãos")
            
        elif escolha == 4:
                print("tente digitar o numero da torre!")
        
        elif escolha == 5:
            rodando == False

'''    




'''pilha.push(2)
pilha.push(4)
pilha.push(6)
pilha.push(8)
pilha.push(10)'''
# fazer: tratar inserção na pilha cheia


# fazer: chamar metodo que imprime a pilha

for i in range(1, 11):
    pilha = PilhaEncadeada1()
    pilha.push(i)
print(f"pilha: {pilha}")
