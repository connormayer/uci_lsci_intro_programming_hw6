import nltk
from nltk.corpus import stopwords
from string import punctuation

# This will download some data you need for word tokenization
# and stopword removal. This might take a few moments the first
# time you run it.
nltk.download('punkt')
nltk.download('punkt_tab') 
nltk.download('stopwords')

# This contains the list of words/punctuation we want to remove
STOP_WORDS = list(punctuation) + ["--", "''", "``"] + stopwords.words('english')

# Your implementation of get_most_frequent_words goes here



# Do not modify the following line
if __name__ == "__main__":
    # Your test code goes here
    pass
