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

def retSentance(l, p,availableCharacters):
    """ Επιστρέφει μια πρόταση τυχαίου μηκους (απο 0 εως l) με p πληθος διαθέσημων λεκτικών"""

    l = random.randint(1, l)  # Οι προτάσεις μπορει να έχουν μήκος απο 1 εως l (πλήθος λεκτικων)
    sentance = ''
    # τα λεκτικά της πρότασης επιλέγονται απο το string availableCharacters εχει len()=p
    for i in range(l):  # επιλέγουμε l λεκτικά (μέγεθος πρότασης)
        tmpChar = availableCharacters[random.randint(0, p - 1)]
        flipChance = random.randint(0, 1)
        if (flipChance == 1):
            tmpChar = tmpChar.swapcase()  # Αναστρέφουμε τον χαρακτήρα
        while (tmpChar in sentance or tmpChar.swapcase() in sentance):  # αν το λεκτικό που επιλεχθηκε ήδη υπάρχει επιλέγουμε αλλο
            tmpChar = availableCharacters[random.randint(0, p - 1)]
            flipChance = random.randint(0, 1)
            if (flipChance == 1):
                tmpChar = tmpChar.swapcase()  # Αναστρέφουμε τον χαρακτήρα
        sentance += tmpChar  # κάθε νεο επιλεγμένο προσθέτεται στην πρόταση


    return sentance


def readKnowledgeBase():
    """ Διαβάζει την βάση γνώσης απο το αρχειο και την επιστρεφει σε πινακα
        returns:(array) πινακας με πρωτη γραμμη τα χαρακτηριστικα (c,l,p)
                οι υπολυπες γραμμες οι προτάσεις """

    c,l,p=retKBcharacteristics()
    i=0
    kb = []
    kbfile = open('knowledgeBase.txt', 'r')
    for line in kbfile:
        if (i==0 or i==1): #αγνωούμε τις 2 πρώτες γραμμές για να κρατήσουμε μόνο την Βάση γνώσης
            if (i == 1):
                characters = line
            i+=1
            continue
        line = line.strip('\n')
        while (len(line)< l):
            line+=' '
        kb.append(line)
    kbfile.close()
    return kb,characters

def retKBcharacteristics():
    """Επιστρέφει τα χαρακτηριστικά της βάσης δεδομένων
    returns:
        c, l, p:
        c (int): Πλήθος πρωτάσεων
        l (int): Μέγιστο πλήθος λεκτικών σε κάθε πρόταση (μέγιστο μήκος πρότασης)
        p (int): Πλήθος διαθέσιμων λεκτικών για κάθε πρόταση
    """
    kbfile = open('knowledgeBase.txt', 'r')
    characteristics = kbfile.readline()
    kbfile.close()
    p, c, l = characteristics.split(',')

    return int(p), int(c), int(l)




def createKnowledgeBase(p, c, l):
    """ Φτιάχνει και επιστρέφει την βάση γνώσης με c πληθος πρωτάσεων
            κάθε πρόταση μήκους 1 εως l
            και πληθος p διαθέσημα λεκτικά για κάθε πρόταση (κάθε προταση εχει διαφορετικά λεκτικά)
        Επίσης η βάση γνώσης γράφεται στο αρχειο knowladgeBase.txt"""

    kb = []
    availableCharacters = "abc"
    for i in range(c+1):
        sentance = ''
        while sentance in kb:
            sentance = retSentance(l, p,availableCharacters)
        kb.append(sentance)

    # Εγραφή της Βάσης σε αρχείο
    knowledgeBaseFile = open('knowledgeBase.txt', 'w')
    knowledgeBaseFile.write(str(p) + ',' + str(c) + ',' + str(l))
    knowledgeBaseFile.write('\n')
    knowledgeBaseFile.write(availableCharacters)
    for i in kb:
        knowledgeBaseFile.write(i)
        knowledgeBaseFile.write('\n')

    knowledgeBaseFile.close()
    return kb
#createKnowledgeBase(3, 5, 3)
