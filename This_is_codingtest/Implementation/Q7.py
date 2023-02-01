score = input()
N = len(score)
half = int(N/2)
answer_before = 0
answer_after = 0

before = score[0:half]
after = score[half:]

for i in range(len(before)):
  answer_before+=int(before[i])

for i in range(len(before)):
  answer_after+=int(after[i])

if answer_before==answer_after:
  print("LUCKY")
else:
  print("READY")