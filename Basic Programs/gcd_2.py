# -*- coding: utf-8 -*-
"""gcd_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m1eI-I93dz83p2X6Gv2w-8PYGeZOgVbk
"""

def gcd(m,n):
  cf=[]
  for i in range(1,min(m,n)+1):
    if (m%i)==0 and (n%i)==0:
      cf.append(i)
  return (cf[-1])

