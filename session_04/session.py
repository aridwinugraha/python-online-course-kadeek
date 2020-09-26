print('# Dictionaries\n')

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

a = {1 : "kadek", 2: "cahya"}
a[3] = "wisnu"
print(a)
a.pop(3)
print(a)
print(a[1])

print()
b = {"depan" : "Kadek", "belakang" : "Cahya" }
print(b["depan"])
print('')

print('# Module and Packages ada di file fibo.py\n')

print('# Error Handling')

while True:
    try :
        a = int(input("masukkan angka : "))
        print(a)
        break
    except :
        print("Salah, masukan angka!")

