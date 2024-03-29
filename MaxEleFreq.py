a = int(input())

arr = list(map(int, input().split()))

mp = {}
for i in arr:
    if i in mp:
        mp[i] += 1
    else :
        mp[i] = 1 


mx_ele = None
mx_val = -1 
for key,value in mp.items():
    if value > mx_val:
        mx_val = value 
        mx_ele = key

print(mx_ele)
