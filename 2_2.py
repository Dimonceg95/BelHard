some_text = input('введите ваше предложение:')
a = str(some_text)
print(a)
b = sorted(a)
print(b)
c = set(some_text)
c = sorted(c)
print(c)

e = [c[i] for i in range(0, len(c))]
print(e)
f = [some_text.count(c[i]) for i in range(0, len(c))]
print(f)
g = dict([((e[m]), (f[m])) for m in range(0, len(c))])
print(g)