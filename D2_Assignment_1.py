string = input("Enter any String")
print('The string is :', string)
dict = {}
reverseDict = {}

for keys in string:
    dict[keys] = dict.get(keys, 0) + 1

[print(key, ' : ', value) for key, value in dict.items()]

for k, v in dict.items():
    reverseDict[v] = reverseDict.get(v, []) + [k]

print("reversedict = ", reverseDict)
