import math

class Node:
    def __init__(self, id):
        self.id = id
        self.layer = 0
        self.input_value = 0
        self.output_value = 0
        self.connections = []
    
    def activate(self):
        if self.layer == 1:
            self.output_value = 1 / (1+math.exp(-self.input_value))
        for i in range(len(self.connections)):
            self.connections[i].to_node.input_value += self.connections[i].weight * self.output_value