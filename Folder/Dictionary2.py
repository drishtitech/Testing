counts=dict()
c=['A','B','A','C']
for name in c:
    counts[name]=counts.get(name,0)+1
print counts
print counts.items()

l=list()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
print l
l[0]=3
print l
l.remove(2)
print l
l.append(6)
l[1]=2
print l
l.sort()
print l
l.pop()
print l
l.reverse()
print l
l.pop(3)
print l
l.append('Aniket')
l.append('Raj')
l.append('Akhilesh')
print l
l.sort()
print l
s="Hello World"
print len(s)
print s[6:11]
print s[0:]
l = len(s)
print l
for i in range(l-1,-1,-1):
	 print s[i]
l=len(s)
i=l-1
print i
while i>=0:
   letter=s[i]
   print letter
   i=i-1
s=(2,)
print type(s)
s=('M','T','W','THU','F','SAT')
print s
a=()
b=('SUN',)
a=b+s
print a
S="HELLO"
for letter in 'HELLO':
    print letter
if 'H' in S:
   print "Correct"
else:
   print "Incorrect"
Great="Hello"
Test=Great.lower()
print Test
print Great
D=Great.find('el')
print D
E=Great
print E
F=E.replace('H','D')
print F
age=25
name='Anil'
print ('{0} is {1} years old'.fromat(name,age))
