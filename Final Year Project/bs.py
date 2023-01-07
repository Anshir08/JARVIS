from collections import defaultdict
n, k = 5, 2
par = [-1,1,2,2,4]
tree = defaultdict(lambda:[])
for i in range(n):
    tree[par[i]].append(i+1)
print(tree)
def dfs(node):
    t = 0
    for i in tree[node]:
        t = max(t,dfs(i)+1)
    return t
    

print(dfs(tree[-1][0]))