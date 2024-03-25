def decimalToBinary(num:int)->str:
    res = ""
    while num > 0:
        if num % 2 == 1:
            res += '1'
        else :
            res += '0'
        num = num // 2
    return res[::-1] 




def binaryTodecimal(num:str)->int:
    n = len(num)
    ans = 0
    var = 0
    for i in range(n-1,-1,-1):
        ans += int(num[i]) * (2**var)
        var += 1
    
    return ans 
    
    
    
t = int(input())
ans = decimalToBinary(t)
decimal = binaryTodecimal(ans)

print(ans,decimal)
