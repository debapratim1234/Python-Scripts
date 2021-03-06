# -*- coding: utf-8 -*-
"""primes_upto_n.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1muJchdRLyiz7r-NU0FvpOJDxPqot3J7Q
"""

def factors(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist = factorlist + [i]
  return(factorlist)
  
def isprime(n):
  return(factors(n)==[1,n])
  
  
def prime(n):
  primelist = []
  for i in range(1,n+1):
    if isprime(i):
      primelist = primelist + [i]
  return primelist

