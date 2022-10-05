def binary_search(nums,start,end):
    if start>end:
        return None;
    mid = (start+end)//2
    if mid == nums[mid]:
        return mid
    elif nums[mid]>mid:
        end = mid-1
        return binary_search(nums,start,end)
    else:
        start = mid+1
        return binary_search(nums,start,end)
        
        
n= int(input())
nums = list(map(int,input().split()))
a = binary_search(nums,0,len(nums)-1)
if a == None:
    print(-1)

else:
    print(a)
    
        