n=int(input())
def fibo(n):
    a = [0] * 1001
    a[1]=1
    a[2]=2

    for j in range(3,n+1):
        a[j] = a[j-1] + a[j-2]
    return a[n] % 10007
print(fibo(n))
#---------------------------------------------- 안되는 이유 [0 for i in range(n+1)]  이것 떄문에 런타임 오류가 남
n = int(input())
a = [0 for i in range(n+1)] 
a[1]=1
a[2]=2

for j in range(3,n+1):
    a[j] = a[j-1] + a[j-2]
print(a[n]%10007)


#----------------------------------------
n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2


for index in range(3, 1001):
    dp[index] = dp[index - 1] + dp[index - 2]
print (dp[n] % 10007)
