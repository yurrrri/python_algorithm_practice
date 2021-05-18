from collections import Counter
import sys

N = int(sys.stdin.readline().rstrip())

m = 0
for _ in range(N):
  l = Counter(map(int, sys.stdin.readline().rstrip().split()))
  two_counts = list(l.values()).count(2) #value값이 2인 수의 개수
  is_two = False
  s = 0

  for key, value in l.items():
    if value==4 and s==0:
      s+=50000+key*5000
    elif value==3 and s==0:
      s+=10000+key*1000
    elif value==2 and two_counts!=2:
      s+=key*100
      is_two = True
    elif value==2 and two_counts==2:
      s+=key*500
      is_two = True
    elif value==1 and s==0:
      s+=max(l.keys())*100
  
  if is_two==True and two_counts==2:
    s+=2000
  elif is_two==True and two_count!=2:
    s+=1000
  m = max(m,s)
print(m)