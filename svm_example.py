
# coding: utf-8

# In[7]:


#import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Import scikit-learn with make_blobs

# In[8]:


from sklearn.datasets.samples_generator import make_blobs


# Create datasets X containing 'n' samples, Y containing two classes

# In[9]:


X, Y = make_blobs(n_samples=500, centers=2, random_state=0, cluster_std=0.40)


# plot scatters

# In[10]:


plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring');
plt.show()


# creating linespace between -1 and 3.5

# In[12]:


xfit = np.linspace(-1, 3.5)


# In[15]:


# plotting scatter
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring')
# plot a line between the different sets of data
for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
    yfit = m * xfit + b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none', 
    color='#AAAAAA', alpha=0.4)
 
plt.xlim(-1, 3.5);
plt.show()

