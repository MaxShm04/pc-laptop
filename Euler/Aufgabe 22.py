text = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ges = 0

with open('p022_names.txt', 'r') as file:
    str = file.read().rstrip().replace('"', "")
    str = str.lower()
    text = str.split(",")
text.sort()
for name in text:
    pos = text.index(name)+1
    sum = 0
    for letter in name:
        sum += (alphabet.index(letter)+1)
    ges += (sum*pos)
    print(pos)
print(ges)


for n in liste == für jedes element n in der liste mache:
