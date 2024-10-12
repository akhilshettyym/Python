# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add('18')
print(s)
print('Yes we can have both 18 as an integer as well as string')