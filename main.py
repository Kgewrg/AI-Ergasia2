import createKnowledgeBase as ckb
import random

def data_structure(chars,kb,binaryvalues):
    p, c, l = ckb.retKBcharacteristics()
    lst=[]
    counter=0
    for i in range(c):
        k = 0
        while (k <= p): # ελέγχουμε αν το κάθε στοιχείο του chars είναι ίσο με το
            if chars[k] in kb[i]:  # εαν το στοιχείο j του chars είναι ίσο με το kb πήγαινε
                if binaryvalues[k] == True:  # εάν είναι true τότε όλη η πρόταση θα είναι true οπότε δεν χρειάζεται περεταίρο αναζήτηση προχωράμε στην επόμενη
                    lst.append(bool(1))
                    break
            elif chars[k].swapcase() in kb[i]:  # εαν το κεφαλαίο στοιχείο του chars είναι ίσο με το kb
                if binaryvalues[k] == False:
                    lst.append(bool(1))
                    break
            if (k == p):
                lst.append(bool(0))
            k+=1
    for i in lst:
        if i == False:
            counter+=1
    lst.append(counter)
    return lst

def flip(values,i):
    binaryvalues=values
    if binaryvalues[i] == True:
        binaryvalues[i] = False
    elif binaryvalues[i] == False:
        binaryvalues[i] = True


def gsat(kb,maxTries,maxFlips):
    kb, characters = ckb.readKnowledgeBase()
    p, c, l = ckb.retKBcharacteristics()
    binaryvalues=[]#μεταβλητή για να κρατάει boolean τιμές στις θέσεις τον λεκτικών
    mincost=l#μεταβλητή για να κρατάει το μικρότερο κόστος των κινήσεων
    breakcondition=0
    data=[]

    for i in range(maxTries): #max προσπάθειες
        if breakcondition == 1:
            break
        for i in range(p):#αναθέτουμε random bool τιμές
            binaryvalues.append(bool(random.getrandbits(1)))
        print(binaryvalues)

        for i in range(maxFlips):
            tmpointer=[] #μεταβλητή που έχει δείκτη/ες από για τις αλλαγές με το μικρότερο κόστος
            tmplist=[] #λίστα για να κρατάει τα κόστη των κινήσεων
            data.append(data_structure(characters,kb,binaryvalues))
            for i in range(p):#συνάρτηση για να βρει τα μέγιστο κόστος
                values=binaryvalues.copy()# το copy χρειάζεται γιατί χωρίς αυτό ο πίνακας values παίρνει τις τιμές του binaryvalues και λειτουργεί σαν δείκτης για τον binary
                flip(values,i)
                tmplist.append(data_structure(characters,kb,values)[-1])#αποθηκεύεται το κόστος της κάθε αλλαγής μέσα στην λίστα
            print("λίστα με τα κόστη",tmplist)
            for i in tmplist: #συνάρτηση για να βρίσκει το μικρότερο κόστος
                if(i < mincost):
                    mincost = i
            print("κοστος",mincost)

            for i in range(len(tmplist)):#λίστα για να κρατάει τους δείκτες των τιμών όπου η αλλαγή τους έχει το μικρότερο κόστος
                if(tmplist[i] == mincost):
                    tmpointer.append(i)
            print("δείκτες kai xaraktires",tmpointer)

            if(len(tmpointer)>1):
                flip(binaryvalues,tmpointer[random.randint(0,len(tmpointer)-1)])
            else:
                print("tmpointer",tmpointer[0])
                flip(binaryvalues,tmpointer[0])
            print(binaryvalues)
            if mincost == 0:
                data.append(data_structure(characters, kb, binaryvalues))
                print(data)
                print("Congrats every sentence in the KB is True ")
                breakcondition=1
                break
            print("--------")


def sentenceFullResolusion(sentance1, sentance2):
    """Υλοποιει την πληρης ανάλυση, αφαιρει τα λεκτικα που εμφανίζονται αντεστραμενα στην αλλη προταση
    parameters:
        sentance1 (string): Η μία πρόταση
        sentance2 (string): Η άλλη πρόταση

    returns:
        result (string): Το αποτέλεσμα της ανάλυσης
    """
    sentance1 = sentance1.strip(' ')
    sentance2 = sentance2.strip(' ')
    validCase = False
    result = sentance1+sentance2
    for i in result:
        if (i.swapcase() in result):
            validCase = True
            result = result.replace(i, '')
            result = result.replace(i.swapcase(), '')
    result = "".join(set(result))  # Αφαιρει τα δυπλοτυπα, προσορινα μετατρεπει το string σε set

    if validCase:
        return result
    else:
        return  # None


def resolution(tmpkb, newCharacter=''):
    """ Υλοποίηση της ανάλυσης μεταξύ της βάσης γνώσης και ένα νέο λεκτικό
        params:
            kb (array): Η βάση γνώσης σε μορφή CNF
            newCharacter (char): Το νέο λεκτικό με το οποίο θα γίνει η ανάλυση
        returns:
            True, kb (array):  Αν γίνεται entailment, η νέα βαση γνώσης
            False:  Αν δεν γίνεται entailment
    """
    tmpkb = tmpkb.copy() # .copy, γιατι αλλιώς αλλάζοντας την βάση γνώσης στην συνάρτηση αλλάζει και στην main
    # Βάζουμε το νέο λεκτικό στην αρχή της βάσης γνώσης για να του δώσουμε προταιρεότητα
    # επίσης το λεκτικό ειναι "γυρισμένο"
    tmpkb.insert(0, newCharacter.swapcase())
    for i in tmpkb:  # Αναλύουμε τις προτάσεις της βάσης γνώσης μεταξύ του
        result = []  # Πινακας που θα αποθυκεύονται τα αποτελέσματα για κάθε πρόταση με όλες τις υπόλοιπες
        for j in tmpkb:
            print("Doing resolution on:", i, j)
            tmpResult = sentenceFullResolusion(i, j)  # Ανάλυση
            if (tmpResult is not None) and (tmpResult not in result) and (tmpResult not in tmpkb):
                # Έλεγος για αν το αποτέλεσμα της ανάλυσης ειναι έγκυρο,
                # (νεα πρόταση) (δεν έχει βρεθεί ήδη) (Δεν είναι ήδη στην βάση γνωσής)
                result.append(tmpResult)

                if ('' in result):  # Έλεγχος για άτοπο
                    tmpkb.pop(0)  # Αφαίρεση του προσορινού γυρισμένου λεκτικού
                    return True, tmpkb  # Γίνεται entailment
                print("resolution:", result)
        tmpkb += result  # Πρόσθεση των νέων προτάσεων που βρέθηκαν

    tmpkb.pop(0)  # Αφαίρεση του προσορινού γυρισμένου λεκτικού
    return False, None





def main():
    kb, characters = ckb.readKnowledgeBase()
    #gsat(kb,10,20)
    print(kb)
    entailed, newkb = resolution(kb, "")
    if newkb is not None:
        # Εγινε το entailement και αρα ενημερώνεται η βαση γνώσης
        kb = newkb


    print(entailed, kb)










if (__name__ == '__main__'):
    main()
