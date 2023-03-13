x = str(input("input string: "))

n = len(x)
l1 = []
l2 = []

if n % 2 == 0:
    c = int(n / 2)
    for i in range(c):
        l1.append(x[i])
        l2.append(x[n - 1 - i])
    if l1 == l2:
        print("Polindrome")
    else:
        print("Not polindrome")
else:
    c = int(n // 2)
    for i in range(c):
        l1.append(x[i])
        l2.append(x[n - 1 - i])
    if l1 == l2:
        print("Polindrome")
    else:
        print("Not polindrome")
    
