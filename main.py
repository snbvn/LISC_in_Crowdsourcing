#main.py
from lisc import Counts
from lisc.utils.db import SCDB
from lisc.utils.io import save_object
import pandas as pd

# Read the terms
terms= pd.read_csv('data.txt', sep=',',header=None)


# Set some new terms
# terms_a = [['crowd','crowdsourcing','crowdsourced','crowdsourced data'],'data crowdsourcing']
# terms_b = [['data','quality', 'data quallity'],['design'],['user interface','UI design','UI']]
terms_a = terms.iloc[0]
terms_b = terms.iloc[1]

# Set terms lists
#  Different terms lists are indexed by the 'A' and 'B' labels
# Initialize counts object
counts = Counts()
counts.add_terms(terms_a, dim='A')
counts.add_terms(terms_b, dim='B')

# Collect co-occurrence data
counts.run_collection()
# Save out the counts object
save_object(counts, 'tutorial_counts', directory=SCDB('lisc_db'))



