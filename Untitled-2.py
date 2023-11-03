class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        popped = self.top
        self.top = self.top.next
        return popped.data

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data

    def get_items(self):
        items = []
        current = self.top
        while current:
            items.append(current.data)
            current = current.next
        return items

def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        disco = origem.pop()
        print(f'Mova o disco {disco} de {origem} para {destino}')
        destino.push(disco)
    else:
        hanoi(n-1, origem, auxiliar, destino)
        disco = origem.pop()
        print(f'Mova o disco {disco} de {origem} para {destino}')
        destino.push(disco)
        hanoi(n-1, auxiliar, destino, origem)

def torre_de_hanoi():
    num_discos = int(input("Digite o número de discos: "))
    
    origem = Pilha()
    destino = Pilha()
    auxiliar = Pilha()

    for disco in range(num_discos, 0, -1):
        origem.push(disco)

    print("\nEstado inicial das pilhas:")
    print("Origem:", origem.get_items())
    print("Auxiliar:", auxiliar.get_items())
    print("Destino:", destino.get_items())

    hanoi(num_discos, origem, destino, auxiliar)

    print("\nEstado final das pilhas:")
    print("Origem:", origem.get_items())
    print("Auxiliar:", auxiliar.get_items())
    print("Destino:", destino.get_items())

if __name__ == "__main__":
    torre_de_hanoi()
