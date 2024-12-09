import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import precision_score

# prepare dataset as  numpy array
df = pd.read_csv('data/train.csv')
# df.loc[df["class"] == "Iris-setosa", "class"] = [0,0,1]
# df.loc[df["class"] == "Iris-versicolor", "class"] = [0,1,0]
# df.loc[df["class"] == "Iris-virginica", "class"] = [1,0,0]
training = df[['sepal_len','sepal_wid','petal_len','petal_wid']].to_numpy()
# standardize the data
training = (training - training.mean())/training.std()

# convert target class to one-hot encodings
target = df['class'].to_numpy()
# print(target)
encoded_target = np.zeros((target.size, target.max()+1), dtype=int)
# print(encoded_target)
encoded_target[np.arange(target.size),target] = 1 
# print(encoded_target)

# build ANN class
class nn():
    def __init__(self, train, target, epoch, lr, input_size, hidden_size, output_size):
        self.training = train
        self.target = target
        self.lr = lr # learning rate
        self.epoch = epoch
        self.log_loss_hist = []
        self.output = []
        # self.w1 = [] # initialize weights randomly using N0,1 normal distribution. A 4 by 4 matrix
        # self.w2 = [] # weights of layer 2. A 4 by 3 matrix
        # self.b1 = []
        # self.b2 = []
        self.w1, self.b1, self.w2, self.b2 = self.initialize_parameters(input_size, hidden_size, output_size)

    def initialize_parameters(self, input_size, hidden_size, output_size):
        # set random seed
        np.random.seed(5467)  # For reproducibility
        weights1 = np.random.randn(input_size, hidden_size) * 0.1
        bias1 = np.zeros((1, hidden_size))
        weights2 = np.random.randn(hidden_size, output_size) * 0.1
        bias2 = np.zeros((1, output_size))
        return weights1, bias1, weights2, bias2
# softmax function. return a numpy array of length 3.
    def softmax(self, x):
        exps = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exps / np.sum(exps, axis=1, keepdims=True)
    # backward propogation for softmax function
    def softmax_backward(self, dA):
        return dA
    
    def relu(self, x):
        return x * (x > 0)
    
    def dReLU(self, x):
        return 1. * (x > 0)

    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))
    
    def sigmoid_backward(self, dA, Z):
        # sig = self.sigmoid(Z)
        return dA * Z * (1-Z) #sig * (1 - sig)
    
    # loss function - nll loss
    def loss(self, data, target):
        nll = -np.dot(np.log(data),target.T)
        return np.sum(nll) / target.shape[0]
        # return -np.mean(data[np.arange(len(target)), target])
    # feed forward network. return a classification in the form of a numpy array of length 3.
    def forward(self, data):
        z1 = np.dot(data, self.w1) + self.b1
        a1 = self.relu(z1)
        # a1 = self.sigmoid(z1)
        z2 = np.dot(a1, self.w2) + self.b2
        a2 = self.softmax(z2)
        # self.output = a2
        return (z1, a1, z2, a2)
# back propogation/weight update
    def backward(self):
        n_samples = self.training.shape[0]
        outputs = self.forward(self.training)
        
        # z1 = outputs[0]
        a1 = outputs[1]
        # z2 = outputs[2]
        a2 = outputs[3]
        # print(len(a1), len(a1[0])) # 90 * 3
        # print(len(a2), len(a2[0])) # 90 * 3
        # Gradient of the loss with respect to z2 (output layer)
        # dz2 = self.target - a1
        dz2 = self.softmax_backward(a2 - self.target) # 90 * 3

        # Gradients for weights2 and bias2
        # dw2 = np.dot(a1.T, dz2) / n_samples
        # dw2 = np.dot(dz2, a2.T) / a2.shape[1] # 90 * 90
        dw2 = np.dot(a2.T, dz2) / a2.shape[1] # 3 * 3
        db2 = np.sum(dz2, axis=0, keepdims=True) / a2.shape[1] #n_samples

        # Gradient of the loss with respect to a1 (hidden layer)
        da1 = np.dot(dz2, self.w2.T) # output dimension 90 * 3
        # da1 = np.dot(self.w2.T, dz2)

        # Gradient of the loss with respect to z1
        # dz1 = da1 * (1 - np.power(a1, 2))
        # dz1 = self.sigmoid_backward(da1, a1) # output dimention 90 * 3, 
        dz1 = self.dReLU(da1)
        # Gradients for weights1 and bias1
        # dw1 = np.dot(self.training.T, dz1) / n_samples
        # dw1 = np.dot(dz1.T, self.training) / self.training.shape[1] # 3 * 4
        dw1 = np.dot(self.training.T, dz1) / self.training.shape[1]
        # db1 = np.sum(dz1, axis=0, keepdims=True) / n_samples
        db1 = np.sum(dz1, axis=0, keepdims=True) / self.training.shape[1]
        return dw1, db1, dw2, db2

    def train(self):
        for _ in range(self.epoch):
            self.output = self.forward(self.training)[3]
            loss = self.loss(self.output, self.target)
            dw1, db1, dw2, db2 = self.backward()
            self.w1 -= self.lr * dw1
            self.w2 -= self.lr * dw2
            self.b1 -= self.lr * db1
            self.b2 -= self.lr * db2

            if _ % 100 == 0:
                print(f'Epoch {_}, Loss: {loss}')
                self.log_loss_hist.append(loss)
# classifies a given object
    def classify(self, data):
        classification = self.forward(data)[3] #self.softmax(self.forward(data))
        classification = np.argmax(classification)
        if classification == 0:
            return 'Iris-virginica'
        if classification == 1:
            return 'Iris-versicolor'
        else:
            return 'Iris-setosa' 
        
    def get_accuracy(self, y_hat):
        y_pred = np.argmax(self.output, axis = 1)
        return precision_score(y_hat, y_pred, average='weighted')
    def validate(self):
        pass

    def test(self):
        pass
        

if __name__ == '__main__':
    # n = nn(training, encoded_target, 3000, 0.002, 4, 4, 3)
    n = nn(training, encoded_target, 2000, 0.001, 4, 3, 3)
    n.train()
    # print(n.output)
    print(n.get_accuracy(target))
    # Plot the log loss over epochs
    sns.lineplot(x=list(range(len(n.log_loss_hist))), y=n.log_loss_hist)
    plt.show()
    # print(n.clas)






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