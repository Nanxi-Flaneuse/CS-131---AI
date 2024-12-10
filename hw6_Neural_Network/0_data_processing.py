import pandas as pd
from sklearn.preprocessing import StandardScaler

# read iris data as pd dataframe
df = pd.read_csv('data/iris.txt', names = ['sepal_len','sepal_wid','petal_len','petal_wid','class'])
df.loc[df["class"] == "Iris-setosa", "class"] = 2
df.loc[df["class"] == "Iris-versicolor", "class"] = 1
df.loc[df["class"] == "Iris-virginica", "class"] = 0

# prepare normalization of features
columns_to_normalize = ['sepal_len','sepal_wid','petal_len','petal_wid']
# Create a scaler object
scaler = StandardScaler()
# Fit and transform the selected columns
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# split dataset into training, validation, and testing, with data size 6:2:2. Draw the same proportion of sample from each categories.
train = pd.concat([df.loc[df['class'] == 2].sample(frac = 0.6), df.loc[df['class'] == 1].sample(frac = 0.6), df.loc[df['class'] == 0].sample(frac = 0.6)], axis = 0)
no_train = df.drop(train.index)
test = pd.concat([no_train.loc[no_train['class'] == 2].sample(frac = 0.5), no_train.loc[no_train['class'] == 1].sample(frac = 0.5), no_train.loc[no_train['class'] == 0].sample(frac = 0.5)], axis = 0)
validate = no_train.drop(test.index)

train.to_csv('data/train.csv', encoding = 'utf-8') 
test.to_csv('data/test.csv', encoding = 'utf-8')
validate.to_csv('data/validate.csv', encoding = 'utf-8')

if __name__ == '__main__':
    pass

'''references:
1. https://stackoverflow.com/questions/38139306/split-dataframe-in-3-subgroups
2. https://www.geeksforgeeks.org/how-to-read-text-files-with-pandas/
3. https://www.geeksforgeeks.org/how-to-concatenate-two-or-more-pandas-dataframes/
4. https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.StandardScaler.html

'''