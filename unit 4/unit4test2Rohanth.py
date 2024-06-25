import random

def random_word():
    word = ''
    length = random.randint(3, 7)
    for i in range(length):
        letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        word+= letter
    return word

def random_sentence():
    sentence = ''
    length = 5
    for i in range(length):
        sentence += random_word() + ' '
    return sentence


def clean_sentence(sentence):
    for i in sentence:
        if ord(i) not in range(97,123):
            sentence = sentence.replace(i,"")
    return sentence

def counts(sentence):
    sentence = clean_sentence(sentence)
    numVowels = 0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'i' or i == 'u':
            numVowels +=1
    percentVowels = 100*(numVowels / len(sentence))
    numConsonants = len(sentence) - numVowels
    percentConsonants = 100*(numConsonants / len(sentence))
    return numVowels, percentVowels, numConsonants, percentConsonants

# Main code
runs = 0
totalVowelsPercentage = 0
totalConsonantsPercentage = 0
while runs < 10:
    sentence = random_sentence()
    vowels, percentV, consonants, percentC = counts(sentence)

    totalVowelsPercentage += percentV
    totalConsonantsPercentage += percentC

    print(sentence, end=" "*(50-len(sentence)))
    print("The sentence is %.2f%% vowels and %.2f%% consonants." % (percentV, percentC))
    runs+=1

avgV = totalVowelsPercentage/10
avgC = totalConsonantsPercentage/10
print("\nThe average percentage of vowels in the 10 sentences is %.2f%%" % avgV)
print("The average percentage of consonants in the 10 sentences is %.2f%%" % avgC)


