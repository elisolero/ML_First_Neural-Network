from numpy import exp,array,random,dot


class NeuralNetwork():

    def __init__(self):
        # get random int 1-10
        random.seed(1)
        self.weights = 2 * random.random((3, 1)) - 1






if __name__ == "__main__":
    NeuralNetwork = NeuralNetwork()

    print (NeuralNetwork.weights)