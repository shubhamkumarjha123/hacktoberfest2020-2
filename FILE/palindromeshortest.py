
# Python3 program to find the shortest 
# palindromic substring 
 
# Function return the shortest 
# palindromic substring 
def ShortestPalindrome(s): 
 
    n = len(s)
    ans = s[0] 
       
    # Finding the smallest character 
    # present in the string 
    for i in range(1, n): 
        ans = min(ans, s[i])
 
    return ans 
 
# Driver code
s = input()
       
print(ShortestPalindrome(s))
