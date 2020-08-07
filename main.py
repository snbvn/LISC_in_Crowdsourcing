#main.py
from lisc import Counts
from lisc.utils.db import SCDB
from lisc.utils.io import save_object

# Read the terms
# terms= pd.read_csv('data.txt', sep=',',header=None)


# Set some new terms
terms_a = [['crowd','crowdsourcing','crowdsourced','Citizen science'],['data crowdsourcing','crowdsourced data']]
terms_b = [['data','quality', 'data quallity'],['design','user interface','UI design','UI']]

# Set terms lists
#  Different terms lists are indexed by the 'A' and 'B' labels
# Initialize counts object
counts = Counts()
counts.add_terms(terms_a, dim='A')
counts.add_terms(terms_b, dim='B')



# Save out the counts object
save_object(counts, 'tutorial_counts', directory=SCDB('lisc_db'))



