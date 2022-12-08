import lib

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL

out = 0
for n in range(1, 1001):
    out += n**n
print(str(out)[-10:])