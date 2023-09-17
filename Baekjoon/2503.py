n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for a in range(1, 10):  # 1부터 9사이의 수 3가지로 이루어진 3자리 수
  for b in range(1, 10):
    for c in range(1, 10):
      if a == b or b == c or c == a:
        continue

      num = list(map(int, str(a) + str(b) + str(c)))

      cnt = 0
      for h in hint: # 각 힌트마다 123 부터 999까지의 조합이 주어진 힌트의 조건과 얼마나 일치하는지를 비교
        number, strike, ball = h[0], h[1], h[2]
        number = list(map(int, str(number)))

        strike_count = 0
        ball_count = 0
        
        for i in range(3):  # 조건 비교 --> 만약 자리에 같은 수가 있다면 strike, 그게 아니더라도 포함되어있다면 ball
          if num[i] == number[i]:
            strike_count += 1
          elif num[i] in number:
            ball_count += 1

        if strike_count == strike and ball_count == ball:  # 조건이 같다면 cnt + 1
          cnt += 1

      if cnt == n:   # 만약 조건을 다 세어봤더니 모든 조건(n)과 일치할 경우 answer + 1
        answer += 1

print(answer)