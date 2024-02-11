#change this
f = open("Poem Of Knowledge.txt", "r")
#change this
ct = [17,73,24,55,84,101,141,44,54,49,10,123,62,131,114,67,47,46,60,83,84]
corpus = f.read()

#Strip new lines, extra spaces, etc.
corpus = corpus.replace('\r', ' ').replace('\n', ' ')
corpus = corpus.replace('  ', ' ')
print(corpus)

#Generate array of words
words = []
buf = ""
for i in range(len(corpus)):
    if corpus[i] == ' ':
        words.append(buf)
        buf = ""
    else:
        buf += corpus[i]
if buf != "":
    words.append(buf)

#Beale's cipher (case sensitive)
flag = ""
for i in range(len(ct)):
    flag += words[ct[i]-1][0]
print(flag)
