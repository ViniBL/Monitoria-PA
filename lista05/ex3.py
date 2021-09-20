l = []
while True:
    n = input()
    if n == 's':
        break
    l.append(int(n))
    
n_l = int(input())
n_c = int(input())
if n_l*n_c != len(l):
    print('IMPOSSIVEL')
else:
    
    m = [[0 for c in range(n_c)] for r in range(n_l)]

    pos = 0
    for i in range(n_l):
        for j in range(n_c):
            m[i][j] = l[pos]
            pos += 1
            
    for i in range(n_l):
        for j in range(n_c):
            print(m[i][j],end=' ')
        print('')

