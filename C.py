import sys

sys.setrecursionlimit(10000) 
infinity = float('inf')

def solve_recursive(mp, memo, x, y, n, m):
    if x < 0 or y < 0:
        return infinity
    if mp[x][y] == -1:
        return infinity
    if x == 0 and y == 0:
        return mp[0][0]
    if memo[x][y] != -1:
        return memo[x][y]
    
    cost_from_up = solve_recursive(mp, memo, x-1, y, n, m)
    cost_from_left = solve_recursive(mp, memo, x, y-1, n, m)
    current_cost = mp[x][y] + min(cost_from_up, cost_from_left)
    memo[x][y] = current_cost
    
    return current_cost

def main():
    n, m = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(n)]
    if mp[0][0] == -1 or mp[n-1][m-1] == -1:
        print("nga bisa sampai nih!")
        return
    memo = [[-1] * m for _ in range(n)]
    result = solve_recursive(mp, memo, n-1, m-1, n, m)
    if result == infinity:
        print("nga bisa sampai nih!")
    else:
        print(int(result))

main()