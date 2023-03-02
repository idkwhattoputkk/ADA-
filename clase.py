
# Clase 21/02/2023

def fibo(n):
    a,b = 0,1
    for n in range(2,n+1):
        a,b = b, a+b
    return b
    
for i in range(100):
    print(fibo(i))

def fibo2(n):
    return None

#Clase 23/02/2023

def ssum(A,n,x):
    ans = None
    if n==0:
        ans = x == 0
    else:
        # if A[n-1]>x:
        #     ans = ssum(A,n-1,x)
        # else:
        #     ans = ssum(A,n-1,x-A[n-1]) or sum(A,n-1,x)
        ans = ssum(A,n-1,x)
        if A[n-1] <= x:
            ans = ans or ssum(A,n-1,x-A[n-1])
    return ans
## con memorizacion
def ssum_memo(A,n,x,mem):
    ans, key = None, (n,x)
    if key in mem:
        ans=mem[key]
    else:
        if n==0: ans = x==0
        else:
            ans=ssum_memo(A,n-1,x,mem)
            if A[n-1] <= x: ans = ans or ssum_memo(A,n-1,x-A[x-1],mem)
        mem[key] = ans
    return ans
## Con tabulacion
def ssum_tab(A,X):
    N = len(A)
    tab = [[None for _ in range(X+1)] for _ in range(N+1)]
    tab[0][0] = True
    for x in range(x+1): tab[0][x] = False
    n,x = 1,0
    while n!=N+1:
        if x ==X+1:
            n,x = n+1,0
        else:
            if A[n-1]>x:
                tab[n][x] = tab[n-1][x]
                
            else:
                tab[n][x] =  tab[n-1][x-A[n-1]] or tab[n-1][x] 
            x+=1
    return tab[N][X]
