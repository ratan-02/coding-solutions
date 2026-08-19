from collections import deque

def find_min_sum(arr):
    n = len(arr)
    if n <= 2:
        return sum(arr)
    
    seen = set()
    queue = deque()
    
    initial_tuple = tuple(arr)
    queue.append(initial_tuple)
    seen.add(initial_tuple)
    
    min_sum = sum(arr)
    
    while queue:
        current = queue.popleft()
        current_sum = sum(current)
        min_sum = min(min_sum, current_sum)
        
        current_list = list(current)
        
        for i in range(1, n - 1):
            new_arr = current_list[:]
            new_arr[i] = current_list[i + 1] + current_list[i - 1] - current_list[i]
            new_tuple = tuple(new_arr)
            
            if new_tuple not in seen:
                seen.add(new_tuple)
                new_sum = sum(new_arr)
                if new_sum < min_sum:
                    queue.append(new_tuple)
                    min_sum = new_sum
    
    return min_sum

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