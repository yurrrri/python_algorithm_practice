import re

string = input()
numbers = re.findall('\d', string)
alphas = re.findall('[a-zA-Z]', string)
alphas.sort()
sum_numbers = 0
for i in numbers:
  sum_numbers+=int(i)

answer = ''.join(alphas)
answer+=str(sum_numbers)

print(answer)