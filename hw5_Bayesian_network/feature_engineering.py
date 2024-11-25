from tsfresh import extract_features
import pandas as pd
import math

# preprocesses the data
with open("data/dataset.txt", "r") as file:
    lines = file.readlines()
lines = [line.split() for line in lines]
lines = [list(map(float, line)) for line in lines]

# make the data into a dataframe for feature extraction
df = pd.DataFrame()
for i, ts in enumerate(lines):
    data = []
    for x in ts:
        if not math.isnan(x):
            data.append([x, i])
    df = df._append(data, ignore_index=True)
df.columns = ['value', 'id']

# perform feature extraction and saves the results to features.csv
if __name__ == '__main__':
    tf = extract_features(df, column_id='id', column_value='value')
    tf.to_csv('features.csv', encoding = 'utf-8')


'''References
1. https://stackoverflow.com/questions/62071901/how-to-use-tsfresh-python-package-to-extract-features-from-time-series-data'''