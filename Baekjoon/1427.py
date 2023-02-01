import sys

numbers = sys.stdin.readline().rstrip()
answer = ""
list = []
for i in numbers:
  list.append(int(i))
list.sort(reverse=True)

for i in list:
  answer+=str(i)
print(answer)