print("Hello World")

# variabel string
a = "Saya"

print(a)

# variabel float
b = 4.0

print(b)

# variabel integer

c = 3

print(c)
print(type(b))

# list

d = []
# tambah list
d.append("Hoo")
d.append(1)
d.append(2)

# tampil list
print(d)

# tampil list dengan perulangan
for x in d:
    print(x)

# operator +-*/%**""+

e = 1 + 2 * 3 / 4.0
print(e)
f = 4 ** 2
print(f)
g = "Hello"+" "+"World"
print(g)
print([1,2,3]*3)

# string formatting

h = "Ari Dwi Nugraha"
i = 22
print("Nama : %s, \nUmur : %d" % (h, i))
