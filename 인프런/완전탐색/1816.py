n = int(input())

def isCorrectPassword(n):
  for i in range(2, 1000001):  # 2<=n<=100만까지의 수에서 하나라도 나눠지는 수가 있다면 바로 비밀번호가 아님을 return하면 됨
    if n%i == 0:
        return "NO"
  return "YES"
  
for _ in range(n):
  m = int(input())
  print(isCorrectPassword(m))