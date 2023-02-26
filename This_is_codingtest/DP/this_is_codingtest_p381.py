n = int(input())
arr = [0] * (n+1)

arr[1] = 2
i2 = i3 = i5 = 1
next2 = 2
next3 = 3
next5 = 5

for i in range(2, n+1):
  arr[i] = min(next2, next3, next5)

  #elif로 하면 틀리는 이유?
  #예를들어 6이나 10과 같은 수는 최소공배수이므로, 같이 수를 높여나가야함
  
  if arr[i] == next2:
    i2+=1
    next2 = arr[i2] * 2
  if arr[i] == next3:
    i3+=1
    next3 = arr[i3] * 3
  if arr[i] == next5:
    i5+=1
    next5 = arr[i5] * 5

print(arr[n])
