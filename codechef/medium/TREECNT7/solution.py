MOD = 998244353

def prufer_to_tree(prufer_seq, n):
    degree = [1] * (n + 1)
    
    for node in prufer_seq:
        degree[node] += 1
    
    edges = []
    
    for node in prufer_seq:
        for i in range(1, n + 1):
            if degree[i] == 1:
                edges.append((node, i))
                degree[node] -= 1
                degree[i] -= 1
                break
    
    remaining = [i for i in range(1, n + 1) if degree[i] == 1]
    if len(remaining) == 2:
        edges.append(tuple(remaining))
    
    return edges

def bfs_color_tree(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    color[1] = 0
    queue = [1]
    
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
    
    return color

def is_good_tree(n, edges, A):
    color = bfs_color_tree(n, edges)
    
    sum_color0 = sum(A[i - 1] for i in range(1, n + 1) if color[i] == 0)
    count_color0 = sum(1 for i in range(1, n + 1) if color[i] == 0)
    
    return sum_color0 == count_color0

def solve():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        
        from itertools import product
        
        if N == 1:
            print(1)
            continue
        
        if N == 2:
            print(1)
            continue
        
        count = 0
        
        for prufer_seq in product(range(1, N + 1), repeat=N - 2):
            edges = prufer_to_tree(list(prufer_seq), N)
            if is_good_tree(N, edges, A):
                count += 1
        
        print(count % MOD)

if __name__ == "__main__":
    solve()