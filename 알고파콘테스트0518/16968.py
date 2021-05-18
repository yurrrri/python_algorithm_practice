import sys

form = sys.stdin.readline().rstrip()
answer = 1
num = 1

if form[0]=='c':
  answer = 26
else:
  answer = 10
for i in range(1, len(form)):
  if form[i]=='c':
    num = 26
  else:
    num = 10
  
  if form[i-1]==form[i]:
    answer *= (num-1)
  else:
    answer *= num

print(answer)