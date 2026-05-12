# this file is for building the inverted index

import nltk
from nltk.corpus import stopwords
from collections import Counter
from collections import defaultdict
from pathlib import Path

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


''' Clean documents 
    Args:
        tokens: uncleaned tokens (lst)'''


def clean_documents(tokens):
    # get english stop words
    stop_words = set(stopwords.words('english'))

    # clean documents
    tokens = [t.lower() for t in tokens]
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stop_words]

    return tokens


''' add book to term document matrix 
    Args: 
        cleaned_tokens: set of cleaned tokens (lst)
        doc_id: id of the document to store (int)
        index: matrix to store the book in (dict)'''


def add_book(cleaned_tokens, doc_id, index):
    # go through words, calculate tf, add the word to the dictionary, store id and tf in the postings

    counts = Counter(cleaned_tokens)

    for term, tf in counts.items():

        if term not in index:
            index[term] = {
                "df": 0,
                "postings": {}
            }

        index[term]["postings"][doc_id] = tf
        index[term]["df"] += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create the inverted index
    index = defaultdict(dict)

    data_path = Path("documents")

    for file_path in data_path.glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

            # tokenize
            tokens = clean_documents(tokenize_files(text))
            # add the terms
            add_book(tokens, 0, index)



