t = int(input())

for _ in range(t):
    k = int(input().split()[1])   # actually reading k, not n
    b = list(map(int, input().split()))
    c = sorted(b)

    if k > 1 or c == b:
        print("YES")
    else:
        print("NO")
