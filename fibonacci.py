#n. fibonacci sayısını bulur.
known={0:0,1:1}
def fibo_rec(n):
 #   if(n<2):
  #      return n
   # else:
    #    return fibo_rec(n-1)+fibo_rec(n-2)
    if n in known:
        #print(known)
        return known[n]
    else:
        result = fibo_rec(n-1)+fibo_rec(n-2)
        known[n]=result
        #print(known)
        return result
print(fibo_rec(10))
