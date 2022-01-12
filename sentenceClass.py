class sentence():
    """Κλαση οπου κρατάει την προταση και τις τιμες κάθε λεκτικού σε δυαδικο
    Κάθε δυαδικη τιμή του λεκτικου, βρίσκεται στην ίδια θεση με το λεκτικο αλλά στον πίνακα sentenceValues

    -- Πιθανότατα να μην χρειάζεται ------
    """

    def __init__(self, sentenceString='', sentenceValues=[]):

        self.sentenceString = sentenceString
        self.sentenceValues = []

        if (len(sentenceValues) > 0):
            # Για την περίπτωση που ο χρήστης έδωσε τιμές για των λεκτικών
            self.sentenceValues = sentenceValues

        else:
            # Ανάθεση δυαδικής τιμής του λεκτικού
            for i in sentenceString:
                if i.isupper():
                    self.sentenceValues.append(1)
                else:
                    self.sentenceValues.append(0)


    def printSentence(self):
        print(self.sentenceString)
        print(self.sentenceValues)

    def sentenceFullResolusion(self, secondSentence):
        """Υλοποιει την πληρης ανάλυση, αφαιρει τα λεκτικα που εμφανίζονται αντεστραμενα στην αλλη προταση
        parameters:
            secondSentence (sentence): Αντικείμενο προτασης με το οποιο θα γίνει η ανάλυση

        returns:
            result (string): Το αποτέλεσμα της ανάλυσης
        """
        result = self.sentenceString+secondSentence.sentenceString
        for i in result:
            if i.swapcase() in result:
                result = result.replace(i, '')
                result = result.replace(i.swapcase(), '')

        return result


