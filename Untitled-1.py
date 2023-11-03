auxiliar = []
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

    def printStack(self):
       
        current = self.top
        while current:
            auxiliar.append(current.data)
            print(current.data, end='  ')
            current = current.next
            
            

# Exemplo de uso da pilha
stack = Pilha()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

#print("Elemento no topo da pilha:", stack.peek())

#print("Pilha:")
stack.printStack()

'''print("Pop:", stack.pop())
print("Pilha após o pop:")
stack.printStack()

'''



print (auxiliar)