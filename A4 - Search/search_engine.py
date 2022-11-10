"""
Thomas Kanenaga
CSE 163 AD

This file creates the SearchEngine class that takes in a file path
and returns a search result within the files found in the path.
"""
from cse163_utils import normalize_token
import math
from document import Document
import os
from operator import itemgetter


class SearchEngine:
    """
    This class represents a corpus of Document objects and includes methods to
    compute the tf–idf statistic between each document and a given query.
    """
    def __init__(self, directory):
        """
        This initializer that takes a str path to a directory and constructs an
        inverted index associating each term in the corpus to the list of
        documents that contain the term.
        """
        self._inverted_index = {}
        self._tot_docs = 0
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            doc = Document(f)
            self._tot_docs += 1
            for word in doc.get_words():
                if word not in self._inverted_index:
                    self._inverted_index[word] = [doc]
                else:
                    self._inverted_index[word].append(doc)

    def _calculate_idf(self, term):
        """
        This method takes a str term and returns the inverse document frequency
        of that term. If the term is not in the corpus, return 0.
        """
        if term not in self._inverted_index:
            return 0
        else:
            tot_docs = self._tot_docs
            tot_docs_term = len(self._inverted_index[term])
            return math.log(tot_docs / tot_docs_term)

    def search(self, string):
        """
        This method takes a str query that contains one or more terms.
        The search method returns a list of document paths sorted in descending
        order by tf–idf statistic. Normalize the terms before processing.
        If there are no matching documents, return an empty list.
        """
        set_doc = set()
        tfidf_docs = []
        # Normalize the terms before processing
        # if multiple words in string it is neccesary to separate them
        sep_string = string.split()
        for string in sep_string:
            string = normalize_token(string)
            # check if word is in keys
            # if string in self._inverted_index:
            # if it is then itterate through each
            # calulating the tfidf score
            # for doc in self._inverted_index[string]:
            # set_doc.add(doc)
            if string in self._inverted_index:
                set_doc.update(self._inverted_index[string])

        for item in set_doc:
            tfidf = 0
            for string in sep_string:
                string = normalize_token(string)
                tf = item.term_frequency(string)
                idf = self._calculate_idf(string)
                tfidf += (tf)*(idf)
            tfidf_docs.append((item.get_path(), tfidf))
        tfidf_docs = sorted(tfidf_docs,
                            key=itemgetter(1), reverse=True)
        # Finally, return the sorted list of documents in descending order
        # according to the tf–idf statistic.
        new_list = []
        for filename in tfidf_docs:
            new_list.append(filename[0])
        return new_list
