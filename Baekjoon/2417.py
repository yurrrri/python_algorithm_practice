n = int(input())
answer = 0

def bs(start, end):
  global answer
  
  while start <= end:
    mid = (start+end) // 2
    
    if mid**2 >= n:
      answer = mid
      end = mid-1
    else:
      start = mid+1

bs(0, n)
print(answer)