## Explanation to Problems

### Problem 1 - LRU Cache

In this problem we had to save and retirve items based on key. For such task python dictionary seemed to be a good choice but it does not have a order, whcich was essential to keep track of usage of elements in cache. Therefore I decied to use OrderedDict.

OrderedDict behaves like a array and dictionary at same time.
set():
If there is space available insert key and value.
If cache is full remove least recently used item using cache.popitem(last=False) and insert new item.

get():
if key exist in cache, we now need to make it most recently used, thus we remove it from cache and add it again.
if key does not exist return 1

Time Complexity: O(1) as get and set operations are done in constant times
Space Complexity: O(n) as memory size depends on cache capacity

### Problem 2 - File Recursion

File system can be thought of as a tree and search for a file with a specific suffix is same as searching for a node with a particular value. So essentially we are using DFS.

If a path is folder, we recursively call all find_files for all its children.
If the path is a file with matching suffix you return that path as array.
function sums up all the paths every time a value is returned.

Time Complexity: O(n) i.e. same as Depth First Search
Space Complexity: O(n) as we need memory for each matching child

### Problem 3 - Huffman Coding

First frequency of each character in input string is counter. After that we start to build huffman tree. We get first two values with lowest value of frequency and create parent node. Add parent in ints correct position in frequency_count dictonary.

After tree is built to encode the data, we traverse tree for each character in string util we encounter node with character same as input character. Add this traversed path to encoded version of input string.

To decode it we traverse the tree until lead node is hit. 0 means go to left and 1 means go to right. Once leaf node is found add character value at that leaf node to decoded version of string.

Time Complexity: O(n) because, to find encoded or decoded version we have to traverse all elements.
Space Complexity: O(n) as there are n nodes in tree

### Problem 4 - Active Directory

We check if user is present in current group's users. If he is we return True else we call same function recursively for all subgroups of current group.

Time Complexity: O(m*n)
first to check if user is in current group's users it takes O(m) m being users in current group
and then recursive calls to all subgroups takes O(n) so in total O(m*n)
Space Complexity: O(1) as we don't store a variable only call function recursively

### Problem 5 - Blockchain

Block chain is an application of linked list. so we can use same structure and operations as that of linked list

Time Complexity:
append: O(1)
search: O(n)
size: O(1)
to_list: O(n)
Space Complexity: O(n) for n blocks in blockchain

### Problem 6 - Union and Intersection

We used linked as base structure and then to perform intersection and union, converted linked list into python list

Time Complexity:
Union: O(n) as we loop through complete array to get uninon.
Intersection: O(n^2) as we loop through first array and then loop again through second array to check if it is present in it.
Space Complexity: O(n) for n elements in linked list
