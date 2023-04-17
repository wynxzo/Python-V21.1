class Node:
    def __init__(self, data):
        self.data = data
        self.sig = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.cabeza = None
        self.tail = None
        
    def add_node(self, data):
        nuevo_node = Node(data)
        
        if self.cabeza is None:
            self.cabeza = nuevo_node
            self.termino = nuevo_node
        else:
            nuevo_node.prev = self.termino
            self.termino.sig = nuevo_node
            self.termino = nuevo_node
            
    def remover_node(self, data):
        current_node = self.cabeza
        
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.sig = current_node.sig
                else:
                    self.cabeza = current_node.sig
                
                if current_node.sig is not None:
                    current_node.sig.prev = current_node.prev
                else:
                    self.termino = current_node.prev
                
                return True
                
            current_node = current_node.sig
        
        return False
    
    def search_node(self, data):
        hoy_node = self.cabeza
        
        while hoy_node is not None:
            if hoy_node.data == data:
                return hoy_node
            
            hoy_node = hoy_node.sig
        
        return None
def print_list(list):
    actual_node = list.cabeza
    
    while actual_node is not None:
        print(actual_node.data)
        actual_node = actual_node.sig

my_list = DoublyLinkedList()
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(3)
my_list.add_node(3)
print_list(my_list)