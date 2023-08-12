from collections import Counter

str = input()
counter = Counter(str)

mid = ''
oddCount = 0

for k, v in list(counter.items()): # {"A": 2, "B": 2}
  if v%2 != 0:
    mid = k  #개수가 홀수인 문자가 있다면, 해당 문자가 가운데 위치하므로 mid에 저장
    oddCount += 1

  if oddCount >= 2: # 개수가 홀수개인 문자가 2개 이상이라면 팰린드롬을 만들 수 없음
    print("I'm Sorry Hansoo")
    exit(0)

result = ''

arr = sorted(counter.items(), reverse=True)
print(arr)
# 오답노트: 내림차순으로 정렬하는 이유? -> 
for k, v in arr:  # 절반만큼 기존 문자열에 더한다음
  result += k * (v//2)

result += mid + result[::-1]  # 위에서 만든 절반만큼의 문자열을 뒤집은것을 더하기
print(result)