1. to run the classifier, simply run classifier.py
2. the output of classifier.py is in the format of a list of classification of all the datapoints in a track followed by the overall clacssification of that track. If you only wish to see the overall result of the entire tracks, refer to detailed instruction in line 66 of classifier.py
3. The additional feature used for classification is the rate of change in speed every second. This was found by looking at the 'value__mean_abs_change' column of the features.csv file, which contains a summary of all the features of the dataset found using the extract_features function of the tsfresh library.
The changes in speed the birds track are significantly larger than the airplane tracks as seen in this column.
4. details of the feature extraction can be found in feature_engineering.py


