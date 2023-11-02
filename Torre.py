escolha = ()

peçassegura = ()

while  escolha !=(int):

    print( " Escolha uma das opçoes:\n 0 - retirar uma peça de lugar \n 1 - colocar uma peça em outro disco\n 2 - mostrar os tres discos\n 3 - mostrar o disco que você está segurando ")    

    escolha = (input())
    print(escolha)
#while True:


    if escolha == 0:
        

    elif escolha == 1:


    elif escolha == 2:



    elif escolha == 3:
        
        if peçassegura == ():
            print("Você nao esta com nenhuma peça em mãos")





class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.cabeca = None

    def push(self, valor):
        novo_no = Noh(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def pop(self):
        removido = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        return removido


pilha = PilhaEncadeada()
pilha.push(2)
pilha.push(4)
pilha.push(6)
pilha.push(8)
pilha.push(10)
# fazer: tratar inserção na pilha cheia


# fazer: chamar metodo que imprime a pilha

print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop()) # fazer: tratar remoção de pilha vazia

