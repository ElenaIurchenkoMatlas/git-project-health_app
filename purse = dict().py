purse = dict()
purse['money'] = 20
purse["candy"] = 2
purse["tissues"] = 1
print(purse)
purse["candy"] = purse["candy"] + 3
print(purse["money"])
print(purse)

# counts = dict()
# print("Enter a line of a text")
# line = input("")
# words = line.split()
# print("Counting...")
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print("Counts", counts)


counts = {"mike":1, "fred": 42, "jan": 100}
for key in counts:
    print(key, counts[key])


mushrooms = {"Oyster": 5, "Button Mushrooms": 8, "Cremini Mushrooms": 2}
print(list(mushrooms))
print(mushrooms.keys())
print(mushrooms.values())
print(mushrooms.items())