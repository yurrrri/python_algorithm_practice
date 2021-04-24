import sys

N = int(sys.stdin.readline())
answer= ""
count = 2

if N==1:
  answer ="1"
elif N==2:
  answer="12"
elif N==3:
  answer="121"
else: # N>3이상인 경우에 계속 비교해 내려가야함
  answer="121"
  while count<N:
     count+=2
     answer+="1"
     if count>N:
       return answer
    if answer[count-2:count]=="12":
      answer+="3"
    else:
      answer+="2"

print(answer)



