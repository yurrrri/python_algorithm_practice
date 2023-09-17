import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()  # 정렬 --> 음수 양수 나누기

left = 0 #시작점
right = n-1 #끝점
answer = abs(arr[left] + arr[right]) #초기 절대값

a = 0
b = 0

while left < right:
    sum = arr[left] + arr[right]
  
    if abs(sum) <= answer:
        answer = abs(sum)
        a = arr[left]
        b = arr[right]

    if sum < 0: #앞을 더 당겨서 음수에서 더 가까워지게 함
      left += 1
    else: # 양수라면 양수 쪽에서 범위를 더 좁힘
      right -= 1
    
print(a, b)      