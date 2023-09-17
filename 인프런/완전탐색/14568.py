candy = int(input())

answer = 0
"""
완전탐색은 결국 탐색의 범위를 정해서, 어떻게 반복문을 2중 3중으로 겹쳐서 그 안에서 해를 찾는지가 핵심임
"""
for a in range(0, candy+1):
  for b in range(0, candy+1):
    for c in range(0, candy+1):
      if a + b + c == candy:
        if a >= b + 2:
          if a != 0 and b != 0 and c != 0:
            if c % 2 == 0:
              answer += 1

print(answer)