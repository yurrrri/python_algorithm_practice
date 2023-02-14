import sys

n = int(sys.stdin.readline().rstrip())
dic = dict()

for _ in range(n):
  num = int(sys.stdin.readline().rstrip())
  if num not in dic:
    dic[num] = 1
  else:
    dic[num] += 1

print(dic.items())
arr = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(arr[0][0]) #맨 첫번째의 [0] key [0]