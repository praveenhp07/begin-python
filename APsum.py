try:
  x1, x2, x3 = raw_input().split()
  n=int(x1)
  a=int(x2)
  d=int(x3)
  sum=(((2*a)+(n-1)*d)*n/2)
  print(sum)
except:
  print("Invalid entry")
