from build_index import IndexManager
from doc_id_manager import DocIdManager


class BooleanQuery:
    def __init__(self):
        self.index_manager = IndexManager()
        self.doc_id_manager = DocIdManager()

    """ Boolean AND. Returns a set of documents that contain both terms
        :arg doc_vec1: document vector for term1 (lst)
        :arg doc_vec2: document vector for term2 (lst)
        :returns intersection list of the document vectors (lst) """

    def boolean_and(self, doc_vec1, doc_vec2):

        intersection = []

        i = 0
        j = 0

        while i < len(doc_vec1) and j < len(doc_vec2):

            # docID in both postings
            if doc_vec1[i] == doc_vec2[j]:
                intersection.append(doc_vec1[i])
                i += 1
                j += 1

            # increment smaller docID
            elif doc_vec1[i] < doc_vec2[j]:
                i += 1

            else:
                j += 1

        return intersection

    """ Boolean OR. Returns a set of documents that contain either terms
            :arg doc_vec1: document vector for term1 (lst)
            :arg doc_vec2: document vector for term2 (lst)
            :returns union list of the document vectors (lst) """

    def boolean_or(self, doc_vec1, doc_vec2):

        union = []

        i = 0
        j = 0

        while i < len(doc_vec1) and j < len(doc_vec2):

            # same docID in both postings
            if doc_vec1[i] == doc_vec2[j]:
                union.append(doc_vec1[i])
                i += 1
                j += 1

            # smaller docID first
            elif doc_vec1[i] < doc_vec2[j]:
                union.append(doc_vec1[i])
                i += 1

            else:
                union.append(doc_vec2[j])
                j += 1

        # add remaining elements
        while i < len(doc_vec1):
            union.append(doc_vec1[i])
            i += 1

        while j < len(doc_vec2):
            union.append(doc_vec2[j])
            j += 1

        return union

    """ Boolean NOT. Returns the docIDs that do not contain a term.
        :arg term: the term to NOT"""

    def boolean_not(self, term):
        # get all docID's from the map file
        all_docs = self.doc_id_manager.get_all_id()
        # get the term docIDs from the index
        term_set = self.index_manager.get_term_vector()
        # return the full docID set minus the term set
        return all_docs - term_set

    """ Solves a tokenized boolean query. Returns a set of docIDs
    which satisfies the query conditions."""

    def answer(self, tokenized_expression):
        stack = []
        operators = [":and:", ":or:", ":not:", "("]

        for token in tokenized_expression:

            if token in operators:
                stack.append(token)
            elif token == ")":
                result = self.solveExpression(stack)
                stack.append(result)
            else:
                v = self.index_manager.get_term_vector(token)  # lookup the term vector
                stack.append(v)

        return stack

    """ Helper function for answer. Solves the subexpression at a given level
    of a boolean query."""

    def solveExpression(self, stack):
        answer = stack.pop()
        token = stack.pop()

        while token != ")":
            if token == ":not:":
                answer = self.boolean_not(answer)
            if token == ":and:":
                operand = stack.pop()
                answer = self.boolean_and(answer, operand)
            if token == ":or:":
                operand = stack.pop()
                answer = self.boolean_or(answer, operand)
            token = stack.pop()

        return answer
