"""
Tree Counting Problem Solution

Key Insight:
A tree is "good" if and only if for its bipartite coloring, 
the sum of array values at nodes of one color equals 
the count of nodes of that color.

Why? 

MOD = 998244353

def prufer_to_tree(prufer_seq, n):
    """Convert Prüfer sequence to edge list using standard algorithm"""
    degree = [1] * (n + 1)  # degree[0] unused, nodes 1 to n
    
    for node in prufer_seq:
        degree[node] += 1
    
    edges = []
    
    # For each element in Prüfer sequence
    for node in prufer_seq:
        # Find the smallest leaf (degree 1)
        for i in range(1, n + 1):
            if degree[i] == 1:
                edges.append((node, i))
                degree[node] -= 1
                degree[i] -= 1
                break
    
    # Connect the last two nodes with degree 1
    remaining = [i for i in range(1, n + 1) if degree[i] == 1]
    if len(remaining) == 2:
        edges.append(tuple(remaining))
    
    return edges

def bfs_color_tree(n, edges):
    """2-color the tree using BFS"""
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
    """
    Check if tree is good for array A.
    A tree is good iff sum of A values in one color class 
    equals the size of that color class.
    """
    color = bfs_color_tree(n, edges)
    
    # Sum values for nodes of color 0
    sum_color0 = sum(A[i - 1] for i in range(1, n + 1) if color[i] == 0)
    count_color0 = sum(1 for i in range(1, n + 1) if color[i] == 0)
    
    # Check if one color class is balanced
    return sum_color0 == count_color0

def solve():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        
        # Count good trees
        from itertools import product
        
        if N == 1:
            print(1)
            continue
        
        if N == 2:
            print(1)
            continue
        
        count = 0
        
        # Generate all possible Prüfer sequences (n^(n-2) total)
        for prufer_seq in product(range(1, N + 1), repeat=N - 2):
            edges = prufer_to_tree(list(prufer_seq), N)
            if is_good_tree(N, edges, A):
                count += 1
        
        print(count % MOD)

if __name__ == "__main__":
    solve()