# this file can be for building the inverted index

import nltk
from nltk.corpus import stopwords
from collections import Counter
from collections import defaultdict

nltk.download('stopwords')
nltk.download('punkt_tab')

''' read the text file in as a string 
    args: 
        file_name: name of the file (str)'''


def read_files(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


''' tokenize the files
    Args:
        text: the text to tokenize (str)'''


def tokenize_files(text):
    return nltk.tokenize.word_tokenize(text, "english", False)


''' Clean documents '''


def clean_documents(tokens):
    # get english stop words
    stop_words = set(stopwords.words('english'))

    # clean documents
    tokens = [t.lower() for t in tokens]
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stop_words]

    return tokens


''' add book to term document matrix '''


def add_book(cleaned_tokens, doc_id):
    # go through words, calculate tf, add the word to the dictionary, store id and tf in the postings
    index = defaultdict(dict)

    counts = Counter(cleaned_tokens)

    for term, tf in counts.items():
        index[term][doc_id] = tf

    return index


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doc = read_files("documents/hamlet.txt")
    tokens = clean_documents(tokenize_files(doc))
    print(tokens)

    print(add_book(tokens, 0))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
