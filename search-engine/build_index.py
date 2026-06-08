# this file is for building the inverted index

import nltk
from nltk.corpus import stopwords
from collections import Counter
from pathlib import Path
import json

from doc_id_manager import DocIdManager

nltk.download('stopwords')
nltk.download('punkt_tab')

''' Handle interaction with the index '''


class IndexManager:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):

        if self._initialized:
            return

        self.index_path = Path("index/index.json")

        if self.index_path.exists():
            with open(self.index_path, "r") as f:
                self.index = json.load(f)
        else:
            self.index = {}

        self._initialized = True

    """ read the text file in as a string
            args:
                file_name: name of the file (str)"""

    @staticmethod
    def read_files(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    ''' tokenize the files
            Args:
                text: the text to tokenize (str)'''

    @staticmethod
    def tokenize_files(text):
        return nltk.tokenize.word_tokenize(text, "english", False)

    ''' Clean documents 
            Args:
                tokens: uncleaned tokens (lst)'''

    @staticmethod
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

    @staticmethod
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

    ''' Build the index from local files. Only adds new files, updates the map file. '''

    def build_index(self):

        # load the map
        manager = DocIdManager()
        id_map = manager.id_map

        data_path = Path("documents")

        for file_path in data_path.glob("*.txt"):

            if file_path.name not in id_map:
                # add document to map
                doc_id = manager.add_file(file_path.name)

                # load document
                doc = self.read_files(file_path)

                # tokenize
                tokens = self.tokenize_files(doc)

                # clean
                cleaned_tokens = self.clean_documents(tokens)

                # add document to index
                self.add_book(cleaned_tokens, doc_id, self.index)

        # save updated index
        self.index_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.index_path, "w") as f:
            json.dump(self.index, f, indent=4)

    def get_index(self):
        return self.index

    def get_term_vector(self, term):
        return list(self.index[term]["postings"].keys())
