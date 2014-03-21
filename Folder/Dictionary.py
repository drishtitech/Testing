counts=dict()
c=['A','B','C','D','A']
for name in c:
  counts[name]=counts.get(name,0)+1
print counts
