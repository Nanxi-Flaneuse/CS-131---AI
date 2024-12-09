import pandas as pd

# read iris data as pd dataframe
df = pd.read_csv('data/iris.txt', names = ['sepal_len','sepal_wid','petal_len','petal_wid','class'])
df.loc[df["class"] == "Iris-setosa", "class"] = 2
df.loc[df["class"] == "Iris-versicolor", "class"] = 1
df.loc[df["class"] == "Iris-virginica", "class"] = 0

# split dataset into training, validation, and testing, with data size 6:2:2
train = df.sample(frac = 0.6)
test = df.drop(train.index).sample(frac = 0.5)
validate = df.drop(train.index).drop(test.index)
train.to_csv('data/train.csv', encoding = 'utf-8') 
test.to_csv('data/test.csv', encoding = 'utf-8')
validate.to_csv('data/validate.csv', encoding = 'utf-8')

if __name__ == '__main__':
    pass

'''references:
1. https://stackoverflow.com/questions/38139306/split-dataframe-in-3-subgroups
2. https://www.geeksforgeeks.org/how-to-read-text-files-with-pandas/

'''