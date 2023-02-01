import sys

wlist = []
klist = []

for _ in range(10):
  wlist.append(int(sys.stdin.readline()))

for _ in range(10):
  klist.append(int(sys.stdin.readline()))

wlist.sort(reverse=True)
klist.sort(reverse=True)

wsum = 0
ksum = 0
for i in range(3):
  wsum+=wlist[i]
  ksum+=klist[i]

print(wsum, ksum)