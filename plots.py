from lisc.utils.db import SCDB
from lisc.utils.io import load_object
from lisc.utils.io import save_object
from lisc.plts.counts import plot_matrix, plot_clustermap, plot_dendrogram
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import savefig
# Reload the counts object from the last tutorial
counts = load_object('tutorial_counts', SCDB('lisc_db'))

# Compute a normalization of the co-occurrence data
counts.compute_score('normalize', dim='A')

# Compute the association index
counts.compute_score('association')
# Check out the computed normalization
# print(counts.score)

# plot the clustermap plot of the association index data
plot_matrix(counts.score, counts.terms['B'].labels, counts.terms['A'].labels)

#save the plot
plt.savefig("output1.png")

# Plot a clustermap of the association index data

plot_clustermap(counts.score, counts.terms['B'].labels, counts.terms['A'].labels)

#save the second plot
plt.savefig("output2.png")


# Plot a dendrogram, to cluster the terms
# plot_dendrogram(counts.score, counts.terms['B'].labels)

#save the second plot
# plt.savefig("output3.png")