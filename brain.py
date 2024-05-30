import node
import connection
import random

class Brain:
    def __init__(self, inputs):
        self.connections = []
        self.nodes = []
        self.inputs = inputs
        self.network = []
        self.layers = 2

        for i in range(self.inputs):
            self.nodes.append(node.Node(i))
            self.nodes[i].layer = 0
        self.nodes.append(node.Node(3))
        self.nodes[3].layer = 0

        self.nodes.append(node.Node(4))
        self.nodes[4].layer = 1

        for i in range(inputs+1):
            self.connections.append(connection.Connection(self.nodes[i], self.nodes[4], random.uniform(-1,1)))
    
    def connect_nodes(self):
        for i in range(len(self.nodes)):
            self.nodes[i].connections = []
        for i in range(len(self.connections)):
            self.connections[i].from_node.connections.append(self.connections[i])
    
    # Orders the network array into inputs, then outputs
    def generate_network(self):
        self.connect_nodes()
        self.network = []

        for j in range(self.layers):
            for i in range(len(self.nodes)):
                if self.nodes[i].layer == j:
                    self.network.append(self.nodes[i])
    
    def feed_inputs(self, data):
        for i in range(self.inputs):
            self.nodes[i].output_value = data[i]
        self.nodes[self.inputs].output_value = 1

        for i in range(len(self.network)):
            self.network[i].activate()
        
        output = self.nodes[self.inputs+1].output_value
        for i in range(len(self.nodes)):
            self.nodes[i].input_value = 0
        
        return output