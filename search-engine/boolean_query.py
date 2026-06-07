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

    @staticmethod
    def boolean_and(doc_vec1, doc_vec2):

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

    @staticmethod
    def boolean_or(doc_vec1, doc_vec2):

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

    def boolean_not(self, term_vector):

        all_docs = set(self.doc_id_manager.get_all_id())
        term_docs = set(term_vector)

        return sorted(all_docs - term_docs)

    """ Tokenize a boolean query 
        :arg
            query: string"""

    @staticmethod
    def tokenize_boolean_query(query):
        # 1. Properly reassign the stripped query
        query = query.strip()
        tokenized_query = []

        i = 0
        # 2. Loop through the entire length of the query
        while i < len(query):
            token = query[i]

            # Handle parentheses
            if token == "(" or token == ")":
                tokenized_query.append(token)
                i += 1

            # Handle operators/fields bounded by colons (e.g., :AND: or field:)
            elif token == ":":
                operator = ":"
                i += 1  # Move past the opening colon

                # Read until the next colon or end of string
                while i < len(query) and query[i] != ":":
                    operator += query[i]
                    i += 1

                if i < len(query):  # Append the closing colon if it exists
                    operator += query[i]
                    i += 1

                operator = operator.lower()
                tokenized_query.append(operator)

            # Handle regular terms/words
            else:
                term = ""
                # Read characters until we hit a special character or space
                while i < len(query) and query[i] not in ["(", ")", ":", " "]:
                    term += query[i]
                    i += 1

                # Only append if we actually collected characters (skips spaces)
                if term:
                    tokenized_query.append(term)

                # If the loop stopped on a space, skip past it
                if i < len(query) and query[i] == " ":
                    i += 1

        return tokenized_query

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

        return stack.pop()

    """ Helper function for answer. Solves the subexpression at a given level
    of a boolean query. Simple AND OR NOT statements. Ex. (t1 :and: t2)"""

    def solveExpression(self, stack):
        answer = stack.pop()
        token = stack.pop()

        while token != "(":
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
