import createKnowledgeBase as ckb
import sentenceClass

def gsat(a,maxTries, maxFlips):
    pass

def main():

    kb = ckb.readKnowledgeBase()
    classedKB = []
    for i in kb:
        classedKB.append(sentenceClass.sentence(i))

    print(classedKB[7].sentenceString, classedKB[8].sentenceString)
    print(classedKB[7].sentenceFullResolusion(classedKB[8]))








if (__name__ == '__main__'):
    main()
