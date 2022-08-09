"""
I need help hacking this word padlock. I set it to a word for my kids 8 years ago and forgot what it is

How do I generate a list of 4 and 5-letter English words that could match this list of letter combinations

MATCH
SOASS
TECN*
ALDEK
BIEYL
CHIAD
DULLY
ERNIN
JNRTA
LTSOE
"""

word_dir = "../LetterSwap/mobywords"

words_4 = set()
words_5 = set()

import glob

for fn in glob.glob(word_dir + "/*.TXT"):
    print("considering fn", fn)

    with open(fn) as f:
        try:
            for line in f:
                line = line.strip()
                if len(line) == 4:
                    words_4.add(line)
                if len(line) == 5:
                    words_5.add(line)
        except UnicodeDecodeError as e:
            pass


def test(w):
    w = w.upper()
    #print("testing", w)
    dials = {0: "MSTABCDEJL",
             1: "AOELIHURNT",
             2: "TACDEILNRS",
             3: "CSNEYALITO",
             4: "HSKLDYNAE"}

    for i in range(len(w)):
        if w[i] not in dials[i]:
            return False, None
    print("found", w)
    return True, w


words = []

for s in [words_4, words_5]:
    for w in s:
        succ, out_word = test(w)
        if succ:
            words.append(w)

print(len(words))

words.sort()
with open("found_words.txt", "wt") as f:
    for w in words:
        f.write(w)
        f.write("\n")

        
