s = "Hello World"
# print(s[::-1])
# rev_s = ' '.join(s.split()[::-1])
# print(rev_s)

words  = s.split()
rev_s = []
for s in range(len(words)-1,-1,-1):
    rev_s.append(words[s])
rev_s = " ".join(rev_s)
print(rev_s)