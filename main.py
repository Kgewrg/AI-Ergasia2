import createKnowledgeBase as ckb



def translate(sentence = ''):
    boolSentence = ''
    for i in sentence:
        if i == '\n':
            continue
        if i.islower():
            boolSentence += str(0)
        else:
            boolSentence += str(1)

    return boolSentence







def gsat(a,maxTries, maxFlips):
    pass




def main():
    kb = ckb.readKnowledgeBase()
    for i in kb:
        print(i)
        print(translate(i))





if (__name__ == '__main__'):
    main()
