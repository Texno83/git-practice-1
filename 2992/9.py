a = input()
cur = a[0]
k = 0
s = ""
s1 = ""
for i in range(len(a)):
	if a[i] != cur:
		s += (cur + str(k))
		k = 1
		cur = a[i]
	elif i + 1 == len(a):
		s += (cur + str(k + 1))
	else:
		k += 1

print(s)

for i in range(len(s)):
	if s[i].isdigit():
		s1 += cur * int(s[i])
	else:
		cur = s[i]

print(s1)

