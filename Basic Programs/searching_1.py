# -*- coding: utf-8 -*-
"""Searching_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/197EVI7JmjU_3HtRv1Po_GcFxSxz_GrNq
"""

# Search for a value in a list
def findpos(l,v):
  (pos,i) = (-1,0)
  for x in l:
    if x == v: # Exit, report position of x
      pos = i
      break
    i = i+1
  # If pos is not reset in loop, pos is -1
  return pos

# l=[1,3,2,5,2,9]
# v=2
