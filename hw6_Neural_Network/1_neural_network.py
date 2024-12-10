import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import precision_score

# prepare training dataset as numpy array
df = pd.read_csv('data/train.csv')
# shuffle the dataset
df = df.sample(frac = 1)
training = df[['sepal_len','sepal_wid','petal_len','petal_wid']].to_numpy()

# convert target class to one-hot encodings for training
target = df['class'].to_numpy()
encoded_target = np.zeros((target.size, target.max()+1), dtype=int)
encoded_target[np.arange(target.size),target] = 1 

# preparing the validation dataset
val_df = pd.read_csv('data/validate.csv')
val_df = val_df.sample(frac = 1)
validation = val_df[['sepal_len','sepal_wid','petal_len','petal_wid']].to_numpy()
val_target = val_df['class'].to_numpy()

# preparing the test dataset
test_df = pd.read_csv('data/test.csv')
test_df = test_df.sample(frac = 1)
testing = test_df[['sepal_len','sepal_wid','petal_len','petal_wid']].to_numpy()
test_target = test_df['class'].to_numpy()

# build ANN class
class nn():
    def __init__(self, train, target, epoch, lr, input_size, hidden_size, output_size, seed):
        self.training = train # data for training
        self.target = target # actual results
        self.lr = lr # learning rate
        self.epoch = epoch
        self.log_loss_hist = [] # logs the losses in every 100 epochs
        self.output = [] # remembers the model predicted output
        self.seed = seed # set random seed
        self.w1, self.b1, self.w2, self.b2 = self.initialize_parameters(input_size, hidden_size, output_size) # set biases
    # randomly initialize the weights and biases
    def initialize_parameters(self, input_size, hidden_size, output_size):
        # set random seed
        np.random.seed(self.seed)  # For reproducibility
        weights1 = np.random.randn(input_size, hidden_size) * 0.1
        bias1 = np.zeros((1, hidden_size))
        weights2 = np.random.randn(hidden_size, output_size) * 0.1
        bias2 = np.zeros((1, output_size))
        return weights1, bias1, weights2, bias2
# # softmax function. return a numpy array of length 3.
#     def softmax(self, x):
#         exps = np.exp(x - np.max(x, axis=1, keepdims=True))
#         return exps / np.sum(exps, axis=1, keepdims=True)
#     # backward propogation for softmax function
#     def softmax_backward(self, dA):
#         return dA
    
#     def relu(self, x):
#         return x * (x > 0)
    
#     def dReLU(self, x):
#         return 1. * (x > 0)
    # sigmoid activation function
    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))
    
    # def sigmoid_backward(self, dA, Z):
    #     return dA * Z * (1-Z) 
    
    # MSE loss
    def loss(self, out, Y):
        s =(np.square(out-Y))
        s = np.sum(s)/len(Y)
        return(s)
    
    # feed forward network. return a classification in the form of a numpy array of width 3.
    def forward(self, data):
        z1 = np.dot(data, self.w1) + self.b1
        a1 = self.sigmoid(z1)
        z2 = np.dot(a1, self.w2) + self.b2
        a2 = self.sigmoid(z2)
        self.output = a2
        return z1, a1, z2, a2  
    
    # back propogation
    def backward(self):
        z1, a1, z2, a2 = self.forward(self.training)
        # error in output layer
        d2 =(a2-self.target)
        d1 = np.multiply((self.w2.dot((d2.transpose()))).transpose(), (np.multiply(a1, 1-a1)))
        # Gradient for w1 and w2
        dw1 = self.training.transpose().dot(d1)
        dw2 = a1.transpose().dot(d2)
        db1 = 0
        db2 = 0
        return dw1, db1, dw2, db2

    # training the nn
    def train(self):
        for epoch in range(self.epoch):
            z1, a1, z2, a2 = self.forward(self.training)

            # calculate loss
            loss = self.loss(a2, self.target)
            dw1, db1, dw2, db2 = self.backward() 

            # update weights
            self.w1 -= self.lr * dw1
            self.w2 -= self.lr * dw2
            self.b1 -= self.lr * db1
            self.b2 -= self.lr * db2

            if epoch % 100 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')
                self.log_loss_hist.append(loss)

    # classifies a given object
    def classify(self, data):
        z1, a1, z2, classification = self.forward(data) 
        classification = np.argmax(classification)
        if classification == 0:
            return 'Iris-virginica'
        if classification == 1:
            return 'Iris-versicolor'
        else:
            return 'Iris-setosa' 
    
    # calculating the weighted accuracy score of the predicted output
    def get_accuracy(self, y_hat):
        y_pred = np.argmax(self.output, axis = 1)
        print(y_pred)
        return precision_score(y_hat, y_pred, average='weighted')
        

if __name__ == '__main__':
    # train the nn
    n = nn(training, encoded_target, 10000, 0.008, 4, 3, 3, 54678)
    n.train()
    print('training accuracy:',n.get_accuracy(target))

    # test the nn on the validation set
    n.forward(validation)
    print('validation accuracy:',n.get_accuracy(val_target))

    # test the nn on the test set
    n.forward(testing)
    print('testing accuracy:',n.get_accuracy(test_target))

    # test user inputs here:
    print('user testing output:',n.classify(np.array([[-0.9006811702978088,0.8006542593569032,-1.284406700770579,-1.3129767272601454]])))
    print('user testing output:',n.classify(np.array([[0.7956690159133096,-0.12495760117130933,0.9902214587995143,0.7905907930498337]])))
    
    # Plot the log loss over epochs
    sns.lineplot(x=list(range(len(n.log_loss_hist))), y=n.log_loss_hist)
    plt.show()






'''
References
1. https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1
2. https://www.geeksforgeeks.org/implementation-of-neural-network-from-scratch-using-numpy/
3. https://pyimagesearch.com/2021/05/06/backpropagation-from-scratch-with-python/
4. https://stackoverflow.com/questions/34968722/how-to-implement-the-softmax-function-in-python
5. https://medium.com/deeplearningmadeeasy/negative-log-likelihood-6bd79b55d8b6
6. https://www.geeksforgeeks.org/how-to-convert-an-array-of-indices-to-one-hot-encoded-numpy-array/
7. https://towardsdatascience.com/lets-code-a-neural-network-in-plain-numpy-ae7e74410795
8.https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.precision_score.html

'''