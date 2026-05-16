class BooleanQuery:
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


