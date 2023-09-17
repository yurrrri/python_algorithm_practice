 import sys
sys.setrecursionlimit(10**6)

"""
이 문제를 재귀로 풀면 좋은 이유
재귀: 처음 --> 목표 까지의 상태 정의가 가능하고, 매개변수를 활용하여 로직을 짤 수 있다면 재귀를 떠올리면 좋음
처음 : t, 목표: s 를 기준으로 하여 재귀 실행 / 종료 조건은 탐색할 필요가 더 없거나 멈춰야되는 시점에서 return문 실행
"""

s = input()
t = input()

def canStoT(str):
  if str == s:
    print(1)
    exit()

  if len(str) <= 0:
    return

  if str[-1] == "A":
    tmp = str[:-1] # 조건 1번 --> 마지막을 제외한 문자열 대상 탐색
    canStoT(tmp)

  if str[0] == "B":
    tmp = str[::-1][:-1]  # 조건 2번 --> 먼저 뒤집고 B 제외하기 
    canStoT(tmp)

canStoT(t)
print(0)