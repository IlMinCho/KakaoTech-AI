import sys
input = sys.stdin.readline

N = int(input())

def n_factor(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

print(n_factor(N))


