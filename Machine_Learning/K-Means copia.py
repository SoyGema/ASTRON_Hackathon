""" K-Means.
Implement K-Means algorithm with TensorFlow, and apply it to classify
handwritten digit images. This example is using the MNIST database of
handwritten digits as training samples (http://yann.lecun.com/exdb/mnist/).
Note: This example requires TensorFlow v1.1.0 or over.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
"""

import numpy as np
import pandas as pd
from astropy.table import Table
from sklearn.externals import joblib
from sklearn import cluster,preprocessing
import seaborn as sns
import matplotlib.pyplot as plt


dat = Table.read('high_low_freq_peakedspectrum_table.fits', format='fits')
df = dat.to_pandas()
df.columns

col_names=['S_p','nu_p', 'alpha_thin',  'alpha_thick', 'RA_gleam', 'Dec_gleam']
X=df[col_names]
X=X.dropna()



kmeans_2clusters=cluster.KMeans(n_clusters=2, max_iter=5000)
kmeans_2clusters.fit(X)




labeled_data = X.copy()
labeled_data['label']=kmeans_2clusters.labels_
np.unique(labeled_data['label'])

#Export the classifier to add
joblib.dump(kmeans_3clusters, 'model.joblib')

import pickle
with open('kmeans_model.pkl', 'wb') as model_file:
    pickle.dump(kmeans_3clusters, model_file)


g = sns.pairplot(labeled_data,hue='label', palette='colorblind',size=6,markers=['o','x'])
plt.show()
