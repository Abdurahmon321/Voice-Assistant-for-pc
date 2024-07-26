import nltk


def process_command(command):
    tokens = nltk.word_tokenize(command)
    return tokens
