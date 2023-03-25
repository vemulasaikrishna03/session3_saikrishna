s=[int(x) for x in input().split()]
arr=[]
for i in s:
    arr.append(str(i))
for i in range(len(arr)):
    key=i
    for j in range(i+1):
        if arr[j]+arr[key]<arr[key]+arr[j]:
            arr[key],arr[j]=arr[j],arr[key]
            key=i
print(arr)
            
    
