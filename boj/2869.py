import sys

A, B, V = map(int, sys.stdin.readline().split())

if (V-A)%(B-A)!=0:
  answer = int((V-A)/(B-A))+1
else:
  answer = int((V-A)/(B-A))

print(answer)