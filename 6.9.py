import math 

#absolute value
def abs_sign(a):
  if a >= 0:
    return a
  else:
    return -a

def abs_sqaure(a):
  b = a * a
  return math.sqrt(b)

#sum of 1~n
def sum_n(n):
  s = 0
  for i in range(1, n+1):
    s = s + i
    return s 
  
#other method
def sum_n(n):
  return n * (n + 1) //2

  
 
