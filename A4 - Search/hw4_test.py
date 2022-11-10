"""
Thomas Kanenaga
CSE 163 AD
This file serves as the testing file for the two search engine
files "document.py" and "search_engine.py"
"""


from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine
# from search_engine import SearchEngine


def test_document():
    """
    This method tests the document file for both
    test_frequency() and get_words().
    Special Case in term_frequency() of a word not in the file
    """
    document_1 = Document('/home/testtext/thomastest.txt')
    assert_equals(['hi', 'i', 'am', 'thomas'], document_1.get_words())
    document_2 = Document('/home/testtext/joe.txt')
    assert_equals(['joe', 'joee', 'i'], document_2.get_words())
    assert_equals(0.07142857142857142, document_2.term_frequency('joee'))
    assert_equals(0, document_1.term_frequency('marcus'))


def test_search_engine():
    """
    This method tests the search_engine file for the search() method.
    """
    pathway_1 = SearchEngine('/home/testtext')
    assert_equals(['/home/testtext/joe.txt', '/home/testtext/thomastest.txt'],
                  pathway_1.search("i"))
    assert_equals(['/home/testtext/joe.txt', '/home/testtext/thomastest.txt'],
                  pathway_1.search("i joe"))
    assert_equals(['/home/testtext/the.txt'], pathway_1.search(" the mas "))
    pathway_2 = SearchEngine('/home/other_files')
    assert_equals(['/home/other_files/doc3', '/home/other_files/doc1'],
                  pathway_2.search("love dogs"))
    assert_equals(['/home/other_files/doc1', '/home/other_files/doc2',
                  '/home/other_files/doc3'],
                  pathway_2.search("pets cats, dogs"))
    assert_equals([],
                  pathway_2.search("Marcus"))


def main():
    # Call your test functions here!
    test_document()
    test_search_engine()


if __name__ == '__main__':
    main()
