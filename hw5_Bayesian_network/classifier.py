from speed_distribution import b_speed_likelihood, p_speed_likelihood
from feature_distribution import b_feature_likelihood, p_feature_likelihood
'''naive bayesian classifier vs. Viterbi. How do they relate to each other?'''
class bayesian_classifier():
    # the input 'data' should be a list of numbers
    def __init__(self, data) -> None:
        # removes all NaN values and convert all elements to floats
        self.data = list(map(float, list(filter(('NaN').__ne__, data))))

    # classify each datapoint in the dataset
    def classify_datapoints(self):
            p_bird_init = 0.5
            p_plane_init = 0.5
            classification = []
            prev_data = self.data[0]
            # initial values are calculated without the feature distribution because we can't calculate the speed difference using just one datapoint
            b = p_bird_init * b_speed_likelihood(prev_data)
            p = p_plane_init * p_speed_likelihood(prev_data) 
            # normalizing probabilities
            p_prev_bird = b/(b+p)
            p_prev_plane = p/(b+p)
            if p_prev_bird > p_prev_plane:
                classification.append('b')
            else:
                classification.append('p')
            for d in self.data[1:]:
                # calculates rate of change in speed for classification
                curr_data = (d - prev_data)/prev_data 
                # calculates the likelihood of the current state
                p_curr_bird = (p_prev_bird*0.9 + p_prev_plane*0.1) * b_speed_likelihood(d) * b_feature_likelihood(curr_data)
                p_curr_plane = (p_prev_plane*0.9 + p_prev_bird*0.1) * p_speed_likelihood(d) * p_feature_likelihood(curr_data)
                # normalize the likelihoods
                p_bird = p_curr_bird/(p_curr_bird + p_curr_plane)
                p_plane = p_curr_plane/(p_curr_bird + p_curr_plane)
                # insert classification into the final output
                if p_bird > p_plane:
                    classification.append('b')
                elif p_bird < p_plane:
                    classification.append('a')
                else:
                    classification.append('equally likely')
                # preserve current likelihoods and speed for use in the next cycle
                p_prev_bird = p_bird
                p_prev_plane = p_plane
                prev_data = d
            return classification
    
    # makes the overall classification based on classification of each datapoint
    def classify_general(self):
        return self.most_frequent(self.classify_datapoints())

    # helper function: return the most frequent element in a list
    def most_frequent(self, List):
        return max(set(List), key=List.count)


if __name__ == '__main__':
    # process the raw data before feeding them into the model
    with open("data/testing.txt", "r") as file:
        lines = file.readlines()
    lines = [line.split() for line in lines]
    counter = 0
    for l in lines:
        counter += 1
        c = bayesian_classifier(l)
        # print('datapoint classification:',c.classify_datapoints()) # can comment this line out to see the final results together
        print('final classification for track',counter,':',c.classify_general())
        print('--------------------------------------------------------------------------------------------------')


        

'''references
1. https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/
2. https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
3. Clarification of the problem by my dear friend from the class Abhigya Tamang.
4. ChatGPT and Google explanation of the Naive Bayesian and Viterbi algorithm.
'''