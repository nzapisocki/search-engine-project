class BooleanQuery:
    """ Boolean AND. Returns the documents that contain both terms """

    def boolean_and(self, term1, term2, index):
        postings1 = list(index[term1]["postings"].keys())
        postings2 = list(index[term2]["postings"].keys())

        intersection = []

        i = 0
        j = 0

        while i < len(postings1) and j < len(postings2):

            # docID in both postings
            if postings1[i] == postings2[j]:
                intersection.append(postings1[i])
                i += 1
                j += 1

            # increment smaller docID
            elif postings1[i] < postings2[j]:
                i += 1

            else:
                j += 1

        return intersection
