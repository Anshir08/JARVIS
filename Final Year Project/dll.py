from collections import defaultdict

d = defaultdict(lambda:0)



matrix = [[1,0,1,50],
          [2,0,1,60],
          [1,0,2,70],
          [3,0,1,300],
          [4,0,2,200]]

for i in range(len(matrix)):
    d[matrix[i][0]] += matrix[i][2]*matrix[i][3]


l = sorted(d,key=lambda x: -1*d[x])

print(l[:3])