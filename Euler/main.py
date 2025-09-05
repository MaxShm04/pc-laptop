import math

nk = 3.0
recht = 1.2
mündliche = 2.8

l = [nk, recht, 1.6,1.6,1.6,1.6, 2.5,1.5,1.3,1.9,2.1,1,1,1.8,2.2,1.7,3.3,1.8,2.2,1.3,2.3,2.1,2,2.1,2.4,2.0,1.3,1.9,2.2,1.5,1.2]
pa = 1.6
ba = 2.5

module = ((sum(l)*5)+mündliche*8)/((len(l)*5)+8)
modulenote = float(str(module)[:3])


print(module)
print(modulenote)

abschluss = 0.8 * modulenote + 0.2 * ba

print(abschluss)
abschlussnote = float(str(abschluss)[:3])
print(abschlussnote)

