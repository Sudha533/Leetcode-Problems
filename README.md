Leetcode Problems:
1.	Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string. 
https://leetcode.com/problems/palindromic-substrings/description/?envType=list&envId=55afh7m7

Example 1: Input: s = "abc" Output: 3 Explanation: Three palindromic strings: "a", "b", "c". 
Example 2: Input: s = "aaa" Output: 6 Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Explanation:
The problem is asking us to count how many palindromic words and group of letters are in a given string.

Brute force approach: 
https://www.geeksforgeeks.org/brute-force-approach-and-its-pros-and-cons/
A brute force approach would be to generate all possible substrings of the given string and check if each substring is a palindrome. This approach would have a time complexity of O(n^3) because there are O(n^2) substrings, and for each substring, we need O(n) operations to check if it's a palindrome. While this approach is simple, it's not efficient for large strings.

Optimized approach:
Expanding Outward to Find Palindromes:
Imagine each character in the string as a starting point.
We can check if there's a palindrome by expanding outward from that character.
It's like stretching our arms out to see if we can touch the same letters on both sides.
Two Cases to Consider:
When we expand outward, we consider two cases:
Case 1: Odd-Length Palindromes: We start with a single character as the center and expand equally to the left and right.
Case 2: Even-Length Palindromes: We start with two adjacent characters as the center and expand equally to the left and right from between them.
So, for each character in the string, we can explore outward in both directions to find palindromes. This way, we cover all possible palindromic substrings in the string efficiently. It's like looking for patterns around each letter to find all the palindromes.
Algorithm:
1.	Initialize a variable count to 0. This will keep track of the number of palindromic substrings we find.
2.	Start a loop that goes through each character in the string.
3.	For each character, consider it as the center of a potential palindrome and expand outward to check if it's a palindrome.
4.	We'll handle two cases:
•	For odd-length palindromes: Expand around the current character by moving left and right from it.
•	For even-length palindromes: Expand around the current character and its next character by moving left and right from them.
5.	Every time we find a palindrome, increment the count variable.
6.	After finishing the loop, return the count variable, which now contains the total number of palindromic substrings.
 Initialization and Loop:
The code initializes variables and enters a for loop to iterate over each character in the string s.
First While Loop:
Inside the for loop, there are two while loops. The code enters the first while loop, which checks for odd-length palindromes centered at the current character i.
If the condition of the first while loop fails (i.e., left >= 0 or right < len(s) or s[left] != s[right]), it moves on to the next line after the while loop.
Second While Loop:
If the condition of the first while loop fails, the code then enters the second while loop, which checks for even-length palindromes centered between the current character i and the next character i+1.
Again, if the condition of the second while loop fails, it moves on to the next line after the loop.
Output:
After the loops, the code prints the final count of palindromic substrings.
             Consider the string "abcba":
Start from the first character "a".
Expand outward: "a" is a palindrome, so increment count.
Move to the second character "b".
Expand outward: "b" is a palindrome, so increment count.
Move to the third character "c".
Expand outward: No palindrome found.
Move to the fourth character "b".
Expand outward: "bcb" is a palindrome, so increment count.
Move to the fifth character "a".
Expand outward: "a" is a palindrome, so increment count.
The total count of palindromic substrings is 3 ("a", "b", "bcb").
Time Complexity: 
let's analyze the time complexity:

Loop Through Each Character:
The outer for loop iterates through each character in the string. Since there are n characters in the string, where n is the length of the string, this loop has a time complexity of O(n).
Expanding Outward:
Each of the two while loops may expand outward up to a certain distance, but it's important to note that the maximum number of iterations for each loop is proportional to the length of the string.
In the worst case, each while loop could iterate over the entire length of the string. Therefore, each while loop has a time complexity of O(n).
Overall Time Complexity:
Since the outer for loop runs n times, and each iteration of the loop may involve running both while loops, the overall time complexity is O(n^2).
So, despite running both while loops for each character, the algorithm's time complexity is still O(n^2) because each loop's maximum number of iterations is proportional to the length of the string. This quadratic time complexity indicates that the algorithm's runtime grows quadratically as the size of the input string increases.

Time complexity with example :
Let's break down the time complexity analysis with an example:
Suppose we have the string "abcde":

Outer Loop:
The outer for loop will iterate over each character in the string. For the string "abcde", there are 5 characters, so the outer loop will run 5 times.
Inner Loops:
For each character in the string, we have two inner while loops.
The first inner while loop checks for odd-length palindromes centered at the current character.
The second inner while loop checks for even-length palindromes centered between the current character and the next character.
Both inner while loops may iterate over the entire length of the string, in the worst case.
Let's see how many iterations each inner while loop may take for the given example string "abcde":

For the first inner while loop:
If we consider the character "b" as the center, it may expand outward to check for palindromes like "aba".
Similarly, for each character in the string, it may expand outward up to a certain distance.
In the worst case, it may iterate over the entire string length.
Therefore, the first inner while loop has a maximum of 5 iterations for the string "abcde".
For the second inner while loop:
Similarly, if we consider the characters "b" and "c" as the center, it may expand outward to check for palindromes like "abba".
Again, for each pair of adjacent characters in the string, it may expand outward up to a certain distance.
In the worst case, it may also iterate over the entire string length.
Therefore, the second inner while loop also has a maximum of 5 iterations for the string "abcde".
Overall Time Complexity:
Since both inner while loops run for each character in the string, and each loop has a maximum of 5 iterations, the overall time complexity is O(n^2), where "n" is the length of the string.
So, even though both inner while loops may iterate over the entire string for each character, the time complexity is still quadratic, indicating that the runtime of the algorithm grows quadratically as the size of the input string increases.
Solution:
Count = 0;
For i in range(len(s)):
	Left = I;
               Right = i
    	While i>=0 and i<s(len) and left[i] == right[i]
		Count + =1
                                Left  -=1
 		Right+=1
         Left = i
  Right = i+1
     	While i>=0 and I<len(s) and left[i] == right[i]
		Count + =1
                                  Left -=1
Right+=1
Print(“Total palindromic substrings:”, count)

ARRAY: 
Imagine arrays as a line of boxes where you can store items. Each box has a number, starting from 0. You can easily find what's inside a specific box by knowing its number. Adding a new item to the line or removing an item might take a bit longer if you have to shift many boxes.
Example: If you have a line of boxes with numbers written on them (like [1, 3, 2, 5, 4]), finding the biggest number is like looking through each box to find the largest number written on any of them.
Find an maximum number from an array:
def findMax(arr):
    max_number = float('-inf')
    for num in arr:
        if num > max_number:
            max_number = num
    print(max_number)
arr = [-1,-6,-9,-4,-99]
findMax(arr)

In the context of finding the maximum element in an array, initializing max_element to negative infinity (float('-inf')) is a common technique used to ensure that any element in the array will be greater than the initial value of max_element.
The time complexity for common operations on arrays depends on the specific operation being performed. Here's a breakdown of the time complexities for various array operations:
Accessing an Element by Index:
Time Complexity: O(1)
Explanation: Accessing an element in an array by its index involves a simple calculation to find the memory location where the desired element is stored. This operation takes constant time because it doesn't depend on the size of the array; it directly accesses the memory location based on the index.
Inserting or Deleting an Element:
Worst-Case Time Complexity: O(n)
Explanation: Inserting or deleting an element in an array can be an expensive operation because it may require shifting all subsequent elements to accommodate the change. In the worst-case scenario, when the element to be inserted or deleted is at the beginning of the array, or when appending an element to the end of a full array (resizing), all elements may need to be shifted, resulting in a time complexity of O(n).
Searching for an Element:
Linear Search:
Time Complexity: O(n)
Explanation: In the worst-case scenario, where the desired element is the last element in the array or not present at all, a linear search would require examining every element in the array, resulting in a time complexity of O(n).
Binary Search (on a sorted array):
Time Complexity: O(log n)
Explanation: Binary search works by repeatedly dividing the search interval in half until the target element is found or the interval is empty. This results in a time complexity of O(log n), as the search space is halved with each iteration.
Copying an Array:
Time Complexity: O(n)
Explanation: Copying an array involves iterating over all elements in the array and copying them to a new array. As a result, the time complexity is directly proportional to the number of elements in the array, resulting in O(n) time complexity.
Overall, arrays offer efficient constant-time access to elements by index but may have higher time complexity for insertion, deletion, and searching operations, depending on the specific scenario.





