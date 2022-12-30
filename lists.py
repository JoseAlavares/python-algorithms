class Node:
    def __init__(self, value):
        self.value = value
        self.anterior = None
        self.next_ = None

    def getValue(self):
        return self.value

class List:
    
    def __init__(self):
        self.nodes = []
        self.head = None

    def add(self, value):        
        if len(self.nodes) == 0:
            self.head = value        

        node = Node(value)        
        node.next = None
        
        if len(self.nodes) > 0:
            self.nodes[len(self.nodes) - 1].next_ = value
            print(self.nodes[len(self.nodes) - 1].next_)
            node.anterior = self.nodes[len(self.nodes) - 1].value    

        self.nodes.append(node)
    
    def delete_first(self):
        if len(self.nodes) == 0:
            raise Exception("Error empty list")
                
        first = self.nodes[0]
        self.head = self.nodes[1].value
        self.nodes[1].anterior = None        
        self.nodes = self.nodes[1:len(self.nodes)]
        first = None


    #def delete_last(self):
        #pass

    def print_list(self):
        if len(self.nodes) == 0:
            print("Empty list")
            return

        for node in self.nodes:
            print("Value: ", node.getValue(), "Anterior", node.anterior, "Next: ", node.next_)
        

list_ = List()
list_.add(89)
list_.add(20)
list_.delete_first()
list_.add(90)
list_.print_list()