# -*- coding: utf-8 -*-
"""Insertion_sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FEiJfGU44NZ2icYv2HZBriDDX2gThZT1
"""

def insert_sort(seq):
  for end in range(len(seq)):
    # Build longer and longer sorted slices
    # In each iteration seq[0:end] already sorted
    # Move first element after sorted slice left
    # till its in the correct place
    pos = end
    while pos>0 and seq[pos] < seq[pos-1]:
      (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
      pos = pos-1
  return seq

# seq = [1,3,2,5,2,9]
# insert_sort(seq)

