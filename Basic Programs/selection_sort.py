# -*- coding: utf-8 -*-
"""selection_sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1itODH-spmvq2qtEEP_tPnv9ZLy2KEdX6
"""

def ssort(l):
  # Scan slices l[0:len(l)],l[1:len(l)],...
  for start in range(len(l)):
    # Find minimum value in slice..
    minipos = start
    for i in range(start,len(l)):
      if l[i] < l[minipos]:
        minipos = i
    # ... and move it to the start of the slice
    (l[start],l[minipos]) = (l[minipos],l[start])
  return l

# l = [1,3,2,5,2,9]
# ssort(l)



