1. The original dataset is first standardized and had its classes turned into numbers - setosa = 2, versicolor = 1, and virginica = 0
2. The training, validation, and testing sets of the model contains data size in the porportion of 6:2:2. The data for each set is randomly sampled from the original dataset without repetition, and each set is shuffled. The proportion of each category in each dataset is the same as the proportion in the original dataset.
3. one-hot encoding of flowers used in training: (0,0,1): Iris-setosa. (0,1,0): Iris-versicolor. (1,0,0): Iris-virginica
4. The neural network has one hidden layer. Users can adjust the epochs, learning rate, and dimension of the weights when creating the nn class.
5. The activation functions used in the neural network are sigmoid functions. The loss function calculates mean squared loss.
6. To ensure prediction accuracy, any dataset used for testing should be first standardized, same is true for user inputs.