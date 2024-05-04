# Example String
s="abcba"

#Intialize count
count = 0

# Loop Through each character in the string
for i in range (len(s)):
    #for odd-leng palindrome centered at i
    left = i
    right = i
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count +=1 # increment 1 because we found the palindrome
        #move left and right pointeres outward
        
        left -= 1
        right += 1
        
    
    # For even length palindrome centerd between i and i+1
    left = i
    right = i+1
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1 #increment count because we found a palindrome
        #move left and right pointers outward
        left -= 1
        right += 1
    #output the final count
print("Total palindromic substrings:", count)