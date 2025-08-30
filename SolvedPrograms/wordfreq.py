a =  "Python is a Easy Programing Language.It was very easy to learn"
word = {}
for i in a.split():
    word[i] = word.get(i,0)+1

print(word)