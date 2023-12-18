name_age = {"Jake": 21, "Mike": 32, "Julia": 24}
a = list()
for k,v in name_age.items():
    a.append((v,k))

print(a)
a = sorted(a,reverse=True)
print(a)
