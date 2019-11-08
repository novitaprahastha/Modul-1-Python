#IRISAN 

p = {-4, -3, -2, -1, 0, 1, 2, 3, 4}
q = {-7, -6, -5, -4, -3, -2, -1, 0, 1}
r = {-1, 0, 1, 2, 3, 4, 5, 6, 7}
s = {-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(p.union(q))
print(p.union(r))
print(q.union(r))
print(list(p.union(q)))

#=====================================

a = {2, 3, 5, 9}
b = {5, 7, 9}

print(a.intersection(b))
print(a.union(b))
print(a & (a | b))
print(b & (a | b))
print((a | b) & (a | b))
print((a & b) | (a | b))