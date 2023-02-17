import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

left = 0 #시작점
right = n-1 #끝점
answer = abs(arr[left] + arr[right]) #초기 절대값

a = 0
b = 0

while left < right: #두개가 겹치면 안되므로
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val
  
    if abs(sum) <= answer:
        answer = abs(sum)
        a = arr[left]
        b = arr[right]

    if sum < 0: #앞을 더 당겨서 0과 가깝게 함
      left += 1
    else:
      right -= 1
    
print(a, b)      