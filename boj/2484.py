from collections import Counter
import sys

prizes = []

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
  scores = list(map(int, sys.stdin.readline().rstrip().split()))
  count = Counter(scores)
  two_counts = list(count.values()).count(2)

  for key, value in count.items():
    if value==4:
      prizes.append(50000+key*5000)
    elif value==3:
      prizes.append(10000+key*1000)
    elif value==2:
      prizes.append(1000+key*100)
    elif value==1:
      prizes.append(