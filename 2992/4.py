f = open("text.txt")
a = set()
s1=""
k=0
for row in f:
    for i in range(row.count(" ") + 1):
        s1=row.split(" ")[i]
        if i==row.count(" "): s1=s1[:-1]
        if s1 not in a: a.add(s1)
    print(" ".join(a))
    a.clear()
    
