class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point

        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        for char in self.children:
            results += self.children[char].suffixes(suffix=suffix+char)

        return results


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        root = self.root

        for char in word:
            root.insert(char)
            root = root.children[char]

        root.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        root = self.root
        for ch in prefix:
            if ch in root.children:
                root = root.children[ch]
            else:
                return False

        return root


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# test case 1
print(MyTrie.find('ant').suffixes())
# expected output ['hology', 'agonist', 'onym']

# test case 2
print(MyTrie.find('fu').suffixes())
# expected output ['n', 'nction']

# test case 3
print(MyTrie.find('trie').suffixes())
# expected output []
