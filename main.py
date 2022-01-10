import createKnowledgeBase as ckb

def translate(sentence = ''):
    """ Μετατρεπει μια πρόταση απο sting σε μια σειρα απο 0 και 1
        params:
            sentence (str): Η πρόταση σε μορφη sting (απο αρχειο)

        Returns:
            boolSentance (δεν ξερω ακομα): η πρόταση με μορφή true ή false
        """
    boolSentance = []
    for i in sentence:
        if i == '\n':
            continue
        if i.islower():
            boolSentance.append(0)
        else:
            boolSentance.append(1)

    return boolSentance







def gsat(a,maxTries, maxFlips):
    pass




def main():
    kb = ckb.readKnowledgeBase()
    # for i in kb:
    #     print(i)
    #     print(translate(i))

    a = kb[9]
    b = kb[13]
    print("a:", a, "b:", b)
    print("translated:", translate(a), translate(b))
    print("not of translated a: ", translate(a)&translate(b))
    # TODO: Πως θα γίνονται οι λογικές πράξεις ανάμεσα στις προτάσεις






if (__name__ == '__main__'):
    main()
