# this file can be for building the inverted index

import nltk
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    doc = read_files("documents/pg40868.txt")
    print(doc)
    print(tokenize_files(doc))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
