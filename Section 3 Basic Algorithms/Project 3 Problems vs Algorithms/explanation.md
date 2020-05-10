## Explanation

### Problem 1 Square root

Solution to the problem is similar to binary search. Here we divide search space in two parts and check if square of mid point is larger or smaller than given number. Also since square root of a number can't be more than half of it, we limit search till half of number.

Time Complexity: O(log n) as we use same technique as binary search.
Space Complexity: O(1) as we don't need any additional space

### Problem 2 Search in a Rotated Sorted Array

Solution to the problem is modified version of binary search. Here we divide search space in two parts and and call function for both halves. Then we return maximum of the values returned by two halves.

Time Complexity: O(log n) as we use same technique as binary search.
Space Complexity: In the case of this problem, each call uses O(1) space, the maximum depth of the recursive tree is O(logn) so the space complexity is O(logn)

### Problem 3 Rearrange Array Digits

Solution to the problem is based on merge sort except if we are on the first level of the recursion. In this case, it does the comparison, as usual, but then starts saving the results on alternative lists, which are then returned as the results.

Time Complexity: O(n log n) as we use same technique as merge sort.
Space Complexity: We used O(n/2) space which is same as O(n)

### Problem 4 Dutch National Flag Problem

We maintain pointer of next index to store 0 and 2. The idea is to put 0 and 2 in their correct positions, which will make sure all the 1s are automatically placed in their right positions. If number is 0 or 2 we swap contents of front index and next index location of 0 or 2.

Time Complexity: O(n) as we sort the array in a single traversal.
Space Complexity: O(1) as we don't need any additional space

### Problem 5 Autocomplete with Tries

We used Trie data structure to build autocomplete feature

Time Complexity: Time complexity of searching and inserting from a trie depends on the length of the word and the number of total words. For length m and no. of words n time complexity is `O(m*n)`
Space Complexity: O(n) as in worst case we have node for each character.

### Problem 6 Unsorted Integer Array

we can solve the problem with a single transversal and two variables, as reference for min and max values.

Time Complexity: O(n) as we traverse input single time
Space Complexity: O(1) as we don't need any additional space

### Problem 7 Request Routing in a Web Server with a Trie

We used Trie data structure to build request router in a web server

Time Complexity: O(n) as time complexity of searching and inserting from a trie depends on the length of the path n that’s being searched for
Space Complexity: O(n) as in worst case we have a node for each path block
