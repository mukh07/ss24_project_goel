import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load the pickle file
with open('opengait/modeling/0_heatmap.pkl', 'rb') as f:
    data = pickle.load(f)
    data=np.array(data)
print (data.shape)