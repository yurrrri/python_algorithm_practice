a = input()
b = int(10**(len(a)-1))

for i in a:
    print("[%d]" % (int(i)*b))
    b = int(b/10)
