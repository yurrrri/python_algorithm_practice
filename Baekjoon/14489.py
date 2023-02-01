import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
C = int(sys.stdin.readline().rstrip())

if A+B<C*2: #치킨 두마리 못삼
  print(A+B)
else:
  print(A+B-2*C)