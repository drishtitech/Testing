def outer():
    x=2
    print "x is:",x
    def inner():
      nonlocal x
      x=5
    inner()
    print "X has been changed to",x
outer()
 
