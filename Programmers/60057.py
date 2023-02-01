import sys
s = sys.stdin.readline().rstrip()

for i in range(1, len(s)+1): #문자열 길이:1부터 전체 길이까지
  part = s[:i]
  for j in range(0, i, len(s)):
    if s[j:j+i]