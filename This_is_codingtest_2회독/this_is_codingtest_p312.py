num = input()

if len(num) == 1:
  print(int(num))
  exit(0)

result = int(num[0])
for i in range(1, len(num)):
  if result <= 1 or int(num[i]) <=1 :
    result += int(num[i])
  else:
    result *= int(num[i])

print(result)