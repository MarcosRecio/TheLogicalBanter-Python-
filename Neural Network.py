import numpy

random=numpy.random
dot=numpy.dot
exp=numpy.exp
class neural_network:
    def __init__(self):
        random.seed(1)
        self.weights=2*random.random((3,1))-1

    def train(self,inputs,outputs,num):
            for iteration in range(num):
                output=self.think(inputs)
                error=outputs-output
                adjustment=dot(inputs.T, error*output*(1-output))
                self.weights=self.weights+adjustment
        
    def think(self, inputs):
            return self.__sigmoid(dot(inputs, self.weights))

    def __sigmoid(self,x):
            return 1/(1+exp(-x))

network=neural_network()
inputs=numpy.array([[1,1,1],[1,0,1],[0,1,1],[1,1,0],[0,0,0]])
outputs=numpy.array([[1,1,0,1,0]]).T
network.train(inputs, outputs, 20000)

print( network.think(numpy.array([0,1,0])))