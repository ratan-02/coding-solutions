def find_min_sum(arr):
    n = len(arr)
    if n <= 2:
        return sum(arr)
    
    memo = {}
    
    def dfs(state):
        state_tuple = tuple(state)
        if state_tuple in memo:
            return memo[state_tuple]
        
        current_sum = sum(state)
        min_sum = current_sum
        
        improved = False
        for i in range(1, n - 1):
            new_val = state[i + 1] + state[i - 1] - state[i]
            new_sum = current_sum - state[i] + new_val
            
            if new_sum < min_sum:
                new_state = state[:]
                new_state[i] = new_val
                result = dfs(new_state)
                min_sum = min(min_sum, result)
                improved = True
        
        memo[state_tuple] = min_sum
        return min_sum
    
    return dfs(arr)

def solve():
    t = int(input())
    
    for _ in range(t):
        n, q = map(int, input().split())
        arr = list(map(int, input().split()))
        
        for _ in range(q):
            i, x = map(int, input().split())
            arr[i - 1] = x
            
            result = find_min_sum(arr)
            print(result)

if __name__ == "__main__":
    solve()