import sys

A, B, V = map(int, sys.stdin.readline().split())

if V%(B-A)!=0:
  print(int(V/(B-A))+1)
else:
  print(int(V/(B-A)))