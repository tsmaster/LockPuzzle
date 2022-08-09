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

import glob
import wordfreq

word_dir = "../LetterSwap/mobywords"

filtered_words = set()

for fn in glob.glob(word_dir + "/*.TXT"):
    print("considering fn", fn)

    with open(fn) as f:
        try:
            for line in f:
                line = line.strip()
                if ((len(line) == 4) or
                    (len(line) == 5)):
                    filtered_words.add(line)
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
    #print("found", w)
    return True, w


words = []

for w in filtered_words:
    succ, out_word = test(w)
    if succ:
        freq = wordfreq.word_frequency(w, 'en')
        words.append((freq, w))

print(len(words))

words.sort()
words.reverse()

usedWords = set()

with open("found_words_freq.txt", "wt") as f:
    for freq, w in words:
        u = w.upper()
        if not (u in usedWords):
            print (freq, w)
            f.write(w)
            f.write("\n")
            usedWords.add(u)

        
