T = int(input())
for _ in range(T):
    N = int(input())
    # Maximum rounds = ceiling((4*N - 1) / 3)
    # Which equals (4*N + 2) // 3
    result = (4 * N + 2) // 3
    print(result)