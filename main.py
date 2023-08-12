from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input().rstrip())
board = [[i for i in range(1, n+1)]] # 첫째줄에는 1부터 N까지의 정수가 차례대로 들어가있다.
temp = []  
for _ in range(n):
	temp.append(int(input()))
board.append(temp)

answer = 0
sorted = []
set1 = set()
set2 = set()

def dfs(depth):
	global sorted
	global answer
	global dic
	global dic2

	if depth == n+1:
		return
	
	if depth > 0 and set1 == set2:
		if answer < len(set1):
			answer = len(set1)
			sorted = list(set1)
		
	for i in range(n):
		if i not in set1:
			set1.add(board[0][i])
			set2.add(board[1][i])
			dfs(depth+1)
			set1.remove(board[0][i])
			set2.remove(board[1][i])

dfs(0)
print(answer)
print(sorted)
			