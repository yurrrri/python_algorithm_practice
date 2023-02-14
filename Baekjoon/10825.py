import sys

n = int(sys.stdin.readline().rstrip())
exam_list = []

for _ in range(n):
    exam_list.append(list(sys.stdin.readline().rstrip().split()))

exam_list.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
  print(exam_list[i][0])