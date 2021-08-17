n = int(input("Enter the number of keys in dictionary."))
d = {}
for i in range(n):
    key = int(input("Enter key: "))
    value = input("Enter Value: ")
    print("\n")
    d.update({key: value})


def invert(d = {1: "one", 2: "two", 3: "one"}):
    id = {}
    for i in d.keys():
        id[d[i]] = []
    for i in d.keys():
        id[d[i]].append(i)
    return id
print(invert(d))
