import numpy as np
from scipy.interpolate import interp1d

# Define the range and likelihood values
x_range = np.linspace(0, 200, num=400)  # Define 11 evenly spaced points between 0 and 10
# read data from likelihood.txt. Split into two sets - bird and plane
with open("data/likelihood.txt", "r") as file:
    lines = file.readlines()

# process each line
birds = np.array(list(map(float, lines[0].split())))
planes = np.array(list(map(float, lines[1].split())))

# Create the interpolation function
bird_interlopation = interp1d(x_range, birds, kind='linear', fill_value='extrapolate')
plane_interlopation = interp1d(x_range, planes, kind='linear', fill_value='extrapolate')

# Construct the likelihood function
def b_speed_likelihood(x):
    return bird_interlopation(x)

def p_speed_likelihood(x):
    return plane_interlopation(x)




'''references
1. https://www.google.com/search?q=python+open+text+file+split+by+line&sca_esv=f906251265b5c9a0&rlz=1C5GCCM_en&ei=HbdAZ-KBLdLR5NoPvsa9wQs&ved=0ahUKEwiihIbRs_CJAxXSKFkFHT5jL7gQ4dUDCA8&uact=5&oq=python+open+text+file+split+by+line&gs_lp=Egxnd3Mtd2l6LXNlcnAiI3B5dGhvbiBvcGVuIHRleHQgZmlsZSBzcGxpdCBieSBsaW5lMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYogQYiQUyCBAAGIAEGKIEMggQABiABBiiBEiRFFCIBFiVEnABeACQAQCYAYYBoAGJDaoBBDIuMTO4AQPIAQD4AQGYAg-gAt0MwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAgUQABiABJgDAIgGAZAGCpIHBDIuMTOgB654&sclient=gws-wiz-serp
2. chatgpt consultation on how to construct a likelihood function using dataset
3. https://stackoverflow.com/questions/4004550/converting-string-series-to-float-list-in-python
'''
