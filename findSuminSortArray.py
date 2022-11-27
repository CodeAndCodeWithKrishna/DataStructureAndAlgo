# Example 2: Given a sorted array of unique integers and a target integer, 
# return true if there exists a pair of numbers that sum to target, false otherwise. 
# This problem is similar to Two Sum.

# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, 
# return true because 4 + 9 = 13.

def findSum(a:list,target):
    
    i=0
    j=len(a)-1

    while(i<j):
        sum=a[i]+a[j]
        if(sum==target):
            return True
        elif sum> target:
            j-=1
        else:
            i+=1

    return False

print(findSum([1, 2, 4, 6, 8, 9, 14, 15],13))