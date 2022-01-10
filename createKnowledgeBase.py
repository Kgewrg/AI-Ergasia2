import random


def returnRandomCharacters(p):
    """Επιστρέφει ενα string μεγεθους p με τυχαιους μοναδικους χαρακητρες"""
    characters = 'abcdefghijklmnopqrstunwxyz'  # για αρχη το μεγιστο που μπορει να παρει το p ειναι 26
    retString = ''
    for i in range(p):  # Επιλέγει τυχαία p λεκτικα
        tmpChar = ''
        while tmpChar in retString:  # Συγουρεύεται οτι δεν θα επιλέξει το ίδιο λεκτικό 2 φορες
            tmpChar = characters[random.randint(0, len(characters)-1)]
        retString += tmpChar
    return retString


def flip(c):
    """ Κάνει τον πεζο-κεφαλαίο και τον κεφαλαίο-πεζο """
    if c.islower():
        return c.upper()
    else:
        return c.lower()


def retSentance(l, p):
    """ Επιστρέφει μια πρόταση τυχαίου μηκους (απο 0 εως l) με p πληθος διαθέσημων λεκτικών"""

    l = random.randint(1, l)  # Οι προτάσεις μπορει να έχουν μήκος απο 1 εως l (πλήθος λεκτικων)
    # Ρωτα αν γινεται το l να ειναι 0
    sentance = ''
    availableCharacters = returnRandomCharacters(p)
    # τα λεκτικά της πρότασης επιλέγονται απο το string availableCharacters εχει len()=p
    for i in range(l):  # επιλέγουμε l λεκτικά (μέγεθος πρότασης)
        tmpChar = ''
        while tmpChar in sentance:  # αν το λεκτικό που επιλεχθηκε ήδη υπάρχει επιλέγουμε αλλο
            tmpChar = availableCharacters[random.randint(0, p-1)]
            flipChance = random.randint(0, 1)
            if (flipChance == 1):
                tmpChar = flip(tmpChar)  # Αναστρέφουμε τον χαρακτήρα
            # TODO: ελεγχο για το αν ο not(γυρισμένος) ειναι ήδη στην πρώταση

        sentance += tmpChar  # κάθε νεο επιλεγμένο προσθέτεται στην πρόταση
    return sentance


def readKnowledgeBase():
    """ Διαβάζει την βάση γνώσης απο το αρχειο και την επιστρεφει σε πινακα
        returns:(array) πινακας με πρωτη γραμμη τα χαρακτηριστικα (c,l,p)
                οι υπολυπες γραμμες οι προτάσεις """

    kb = []
    kbfile = open('knowledgeBase.txt', 'r')
    for line in kbfile:
        line = line.strip('\n')
        kb.append(line)

    return kb




def createKnowledgeBase(c=20, l=5, p=10):
    """ Φτιάχνει και επιστρέφει την βάση γνώσης με c πληθος πρωτάσεων
            κάθε πρόταση μήκους 1 εως l
            και πληθος p διαθέσημα λεκτικά για κάθε πρόταση (κάθε προταση εχει διαφορετικά λεκτικά)
        Επίσης η βάση γνώσης γράφεται στο αρχειο knowladgeBase.txt"""
    kb = []
    for i in range(c):
        sentance = ''
        while sentance in kb:
            sentance = retSentance(l, p)
        kb.append(sentance)

    # Εγραφή της Βάσης σε αρχείο
    knowledgeBaseFile = open('knowledgeBase.txt', 'w')
    knowledgeBaseFile.write(str(c)+','+str(l)+','+str(p))
    for i in kb:
        knowledgeBaseFile.write(i)
        knowledgeBaseFile.write('\n')

    knowledgeBaseFile.close()
    return kb
