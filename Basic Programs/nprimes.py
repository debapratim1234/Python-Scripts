# -*- coding: utf-8 -*-
"""nprimes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ooBqPj316MMDhagHoAtbPPL5pVNVu6mP
"""

def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist = factorlist + [i]
  return(factorlist)
  
def isprime(n):
  return(factors(n)==[1,n])

def nprimes(n):
  (count,i,plist) = (0,1,[])
  while(count<n):
    if isprime(i):
      (count,plist) = (count+1,plist+[i])
    i = i+1
  return plist



