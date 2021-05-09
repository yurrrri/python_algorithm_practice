import sys

N = int(sys.stdin.readline().rstrip())
answer = 0

for _ in range(N):
  answer+=int(sys.stdin.readline().rstrip())

answer = answer-(N-1)
print(answer)