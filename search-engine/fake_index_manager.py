class FakeIndexManager:
    """ Mock data to get the docID vector for a term"""

    @staticmethod
    def get_term_vector(term):
        if len(term) % 2 == 0:
            return ['32']
        else:
            return ['69']
