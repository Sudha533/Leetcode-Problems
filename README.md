<p>	Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string. </p>
<a href="https://leetcode.com/problems/palindromic-substrings/description/?envType=list&envId=55afh7m7">Link</a>
<ul>
<li>Example 1: Input: s = "abc" Output: 3 Explanation: Three palindromic strings: "a", "b", "c". </li>
<li>Example 2: Input: s = "aaa" Output: 6 Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".</li>
<ul>
<p>
<b><u>Explanation:</u></b>
The problem is asking us to count how many palindromic words and group of letters are in a given string. Lets use a technique called “expand aound center” to find palindromic substrings efficiently.
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
6.	After finishing the loop, return the count variable, which now contains the total number of palindromic substrings..
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

This approach has a time complexity of O(n^2), where n is the length of the string. Now, let's implement this algorithm.

 