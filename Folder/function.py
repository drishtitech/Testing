def message():
    print "Welcome"
message()
message()
def printmax(a,b):
    if a>b:
      print "a is greater than b"
    elif a==b:
      print "a is equal to b"
    else:
      print "a is smaller than b"
printmax(4,7)
x=6
y=3
printmax(x,y)
x=10
def f1(x):
    print "x is:",x
    x=2
    print "x is now:",x
f1(x)
print "x is:",x
x=50
def f2():
    global x
    print "x is:",x
    x=2
    print "Now x is:",x
f2()
print "Value will be:",x
