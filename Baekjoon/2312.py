import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = int(sys.stdin.readline())
    for i in range(2, a + 1):
        count = 0
        if a % i == 0:
            while a % i == 0:
                a = a // i
                count += 1
            print('%d %d' %(i, count))
        elif a == 1:
            break