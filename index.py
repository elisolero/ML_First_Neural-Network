from numpy import exp,array,random,dot


class NeuralNetwork():

    def __init__(self):

        random.seed(1)  # get random int 1-10
        self.weights = 2 * random.random((3, 1)) - 1 #render weights

    def trainModel(self,training_set_inputs, training_set_outputs, number_of_training_iterations):

        for iteration in xrange(number_of_training_iterations):
            # print(training_set_inputs)
            output = self.think(training_set_inputs)

            error = training_set_outputs - output #t
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Adjust the weights.
            self.weights += adjustment



    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        dotForSigmoid = dot(inputs, self.weights)
        return self.__sigmoid(dotForSigmoid)

    def __sigmoid_derivative(self, x):
        return x * (1 - x)





if __name__ == "__main__":
    NeuralNetwork = NeuralNetwork()

    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    NeuralNetwork.trainModel(training_set_inputs, training_set_outputs, 10000)

    # print NeuralNetwork.think(array([1, 0, 0]))

    print "New synaptic weights after training: "
    print NeuralNetwork.weights

    # Test the neural network with a new situation.
    print "Considering new situation [1, 0, 0] -> ?: "
    print NeuralNetwork.think(array([1, 0, 0]))
