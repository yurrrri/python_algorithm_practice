data = input() # 여러개의 숫자로 구성된 문자열
result = int(data[0])

for i in range(1, len(data)):
  if (result<=1):
    result+=int(data[i])
  else:
    result*=int(data[i])

print(result)
