a = input()
aa = a.split(",")
gh = 0
b = []
hj = 0
for i in range(len(aa)):
    if aa[gh] == "1":
        gh += 1
        hj += 1
    elif aa[gh] == "0":
        b.append(hj)
        b.append(0)
        hj = 0
        gh += 1
if b[-1] != 0 or b[-1] == 0:
    b.append(hj)

print(max(b))