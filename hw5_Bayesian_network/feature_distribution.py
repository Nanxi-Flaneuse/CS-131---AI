import pandas as pd
import numpy as np
from scipy.stats import norm
# extract additional feature from dataset.txt. Construct likelihood function using these features

with open("data/dataset.txt", "r") as file:
    lines = file.readlines()
lines = [line.split() for line in lines]
lines = [list(map(float, line)) for line in lines]
bird = np.array(lines[:10]).transpose()
plane = np.array(lines[10:]).transpose()

# construct a dataframe of the rate of change in speed for the 10 tracks of birds
df_b = pd.DataFrame(bird, columns = ['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10'])
# calculate the pct change between neighboring rows and drop na values
df_b = df_b.pct_change().dropna()
# flattens the data for calculating distribution.
df_b = df_b.to_numpy().flatten()

# construct a dataframe of the rate of change in speed for the 10 tracks of plane
df_p = pd.DataFrame(plane, columns = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10'])
# calculate the pct change between neighboring rows and drop na values
df_p = df_p.pct_change().dropna()
# flattens the data for calculating distribution.
df_p = df_p.to_numpy().flatten()

# construct the likelihood functions for birds and planes
def b_feature_likelihood(x):
    mean, std = np.mean(df_b), np.std(df_b)
    return norm.pdf(x, mean, std)

def p_feature_likelihood(x):
    mean, std = np.mean(df_p), np.std(df_p)
    return norm.pdf(x, mean, std)

'''references:
1. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
2. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html
'''