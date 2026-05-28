#week14-1.py CPE 2026-05-26 26D2 UVA10189
t = 1
while True: #step01
    M,N = list(map(int,input().split())) #step01
    if M == 0 and N == 0: break #step01: input
    a = [] 
    for i in range(M):
        a.append( list(input()) ) #step03:list()
        
    for i in range(M):
        for j in range(N):
            if a[i][j] =='*': continue #step06
            a[i][j] = 0 #step06
            for ii in range(i-1, i+2): #step04
                for jj in range(j-1, j+2):
                    if ii < 0 or jj < 0 or ii>=M or jj>=N:
                        continue #step05    
                    if a[ii][jj] == '*':
                        a[i][j] += 1
     
    if t > 1: print() #step02:output
    print(f'Field #{t}:') #step02:output
    for i in range(M): #step02:output
        for j in range(N):
            print(a[i][j], end='')
        print()
    t += 1