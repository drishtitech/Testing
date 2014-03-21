d={'A':1,'B':2,'C':3,'D':4}
if d.has_key('A'):
    print "A is present in the dictionary"
else:
    print "A is not present in the dictionary"
keys=d.keys()
print keys
keys.sort()
print keys
values=d.values()
print values
values.sort()
print values
print "Numbers:",len(d)
del d['A']
print d
d['E']=6
print d
d['E']=7
print d

