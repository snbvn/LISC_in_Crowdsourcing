
from lisc import Words
from lisc.utils.db import SCDB
from lisc.data import Articles, ArticlesAll
from lisc.utils.io import load_object
from lisc.utils.io import save_object
from lisc.plts.words import plot_wordcloud
import matplotlib.pyplot as plt
# Set up some terms
terms = [['crowdsourcing','crowdsrouced','Citizen science'], ['user interface','UI','quality', 'data quality','information system']]

# Initialize Words object and set the terms to search for
words = Words()
words.add_terms(terms)

# Set up our database object, so we can save out data as we go
db = SCDB('lisc_db')

# Collect words data
words.run_collection(usehistory=True, retmax='100', save_and_clear=True, directory=db)
# Save out the words data
save_object(words, 'tutorial_words', directory=db)

# Reload the words object
words = load_object('tutorial_words', directory=SCDB('lisc_db'))

# Reload all data
for ind in range(words.n_terms):
    words.results[ind].load(directory=db)

# Collect into list of aggregated data objects
all_articles = [ArticlesAll(words[label]) for label in words.labels]
# Plot a WordCloud of the collected data for the first term
# print (all_articles[0].words)
plot_wordcloud(all_articles[0].words, 25)
plt.savefig("output3.png")
# cloud.to_file('output3.png')

# Iterating through articles found from a particular search term
#  The iteration returns a dictionary with all the article data

with open("articles.txt", "w") as file:
    for art in words['crowdsourcing']:
        if art['year']>2018:
            file.write('%s\n' % art['title'])
    