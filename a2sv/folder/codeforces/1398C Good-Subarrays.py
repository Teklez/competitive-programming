t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    count = 0
    preSum = 0
    prev = {0:1}
    for i in range(n):
        preSum += int(a[i])
        count += prev.get(preSum - i - 1, 0)
        prev[preSum - i - 1] = prev.get(preSum - i - 1, 0) + 1
    print(count)