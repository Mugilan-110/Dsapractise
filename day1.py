def printnum(n):
    for i in range(1,n+1):
        print(i)
printnum(5)

def traverse(m):
    for i in range(len(m)):
        for j in range (len(m[i])):
            print(m[i][j])
m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]            
traverse(m)
    