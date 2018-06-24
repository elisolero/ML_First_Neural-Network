from numpy import exp,array,random,dot


class NeuralNetwork():

    def __init__(self):

        random.seed(1)  # get random int 1-10
        self.weights = 2 * random.random((3, 1)) - 1 #render weights

    def trainModel(self,training_set_inputs, training_set_outputs, number_of_training_iterations):

        for iteration in xrange(number_of_training_iterations):
            output = self.think(training_set_inputs)
            print(output)



    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))


    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.__sigmoid(dot(inputs, self.weights))






if __name__ == "__main__":
    NeuralNetwork = NeuralNetwork()

    # print (NeuralNetwork.weights)
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    NeuralNetwork.trainModel(training_set_inputs, training_set_outputs, 10000)