"""
Thomas Kanenaga
CSE 163 AD

This file outlines the class Document
"""
from cse163_utils import normalize_token


class Document:
    """
    This class represents the data in a single web
    page and includes methods to compute term
    frequency. (But not document frequency since
    that would require access to all of the documents
    in the corpus.)
    """
    def __init__(self, file_path):
        """
        This method takes a path to a document and
        initializes the document data and precomputes the
        term frequency for each term in the document in the
        initializer by constructing a dictionary that maps each
        str term to its float term frequency in the given document.
        """
        self._file_path = file_path
        self._tot_term_freq = {}
        self._word_list = []
        self._word_count = 0
        # opens file
        with open(file_path) as f:
            lines = f.readlines()
            for line in lines:
                words = line.split()

            # finds each word and normalizes it then adds it to a list
                for word in words:
                    word = normalize_token(word)
                    self._word_list.append(word)  # adds word to list of words
                    if word not in self._tot_term_freq.keys():
                        self._tot_term_freq[word] = 1
                    else:
                        self._tot_term_freq[word] = \
                            self._tot_term_freq[word] + 1
            for key in self._tot_term_freq:
                self._tot_term_freq[key] = \
                    self._tot_term_freq[key] / len(self._word_list)

    def term_frequency(self, term):
        """
        This method returns the term frequency of a given term by looking
        it up in the precomputed dictionary.If a term does not appear in a
        given document, it should have a term frequency of 0
        """
        term = normalize_token(term)
        if term not in self._tot_term_freq:
            return 0
        else:
            return self._tot_term_freq[term]

    def get_path(self):
        """
        This method returns the path of the file that this document represents.
        """
        return self._file_path

    def get_words(self):
        """
        This method returns a list of the unique, normalized words in
        this document.
        """
        return list(self._tot_term_freq.keys())
