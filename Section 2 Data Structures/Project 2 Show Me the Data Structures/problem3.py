# node object to build the tree
class Node:

    def __init__(self, char=None, count=0, left=None, right=None):
        self.char = char
        self.count = count
        self.left = left
        self.right = right


# create a python dictonary of charcter frequency counts
def get_frequency_count(data):
    frequency_count = {}

    for ch in data:
        if ch in frequency_count:
            frequency_count[ch] += 1
        else:
            frequency_count[ch] = 1

    return frequency_count


# sort frequency_count dictonary based on value
def sort_frequency_count(frequency_count):
    return {k: v for k, v in sorted(frequency_count.items(), key=lambda item: item[1] if type(item[1]) == int else item[1].count)}


# get the first key, value from frequency_count (uses pop)
def get_first_key(frequency_count):
    key = list(frequency_count.keys())[0]
    value = frequency_count.pop(key)
    return (key, value)


# encodes a string
def get_encoded_string(root, string):
    encoded = ""
    for ch in string:
        encoded += get_encoded_char(root, ch)
    return encoded


# find encoded version of a char by traversing huffman tree
def get_encoded_char(root, char, side=""):
    if root:
        if root.char == char:
            return side
        left = get_encoded_char(root.left, char, side=side + "0")
        right = get_encoded_char(root.right, char, side=side + "1")

        if left != None:
            return left
        if right != None:
            return right


# builds huffman tree
def build_huffman_tree(data):
    if data == None or data == "" or data == " ":
        print("Incorrect string provided for building huffman tree")
        return None, None

    frequency_count = get_frequency_count(data)

    while len(frequency_count.keys()) > 1:
        frequency_count = sort_frequency_count(frequency_count)

        key1, value1 = get_first_key(frequency_count)
        key2, value2 = get_first_key(frequency_count)

        if type(value1) == int:
            left = Node(key1, value1)
        else:
            left = value1

        if type(value2) == int:
            right = Node(key2, value2)
        else:
            right = value2

        value1 = value1 if type(value1) == int else value1.count
        value2 = value2 if type(value2) == int else value2.count
        value = value1 + value2

        parent = Node(key1 + key2, value, left, right)

        frequency_count[parent.char] = parent

    root = get_first_key(frequency_count)[1]
    return root, get_encoded_string(root, data)


# decodes huffman encoded string to regular string
def decode_string(tree, encoded_string):

    if encoded_string == None or encoded_string == "":
        print("Incorrect string provided for decoding")
        return None

    decoded_string = ""

    pointer = tree
    while len(encoded_string) > 0 or pointer:
        if pointer.left == None and pointer.right == None:
            decoded_string += pointer.char
            pointer = tree
            if len(encoded_string) == 0:
                break

        direction = encoded_string[0]
        encoded_string = encoded_string[1:]
        if direction == "0":
            pointer = pointer.left
        elif direction == "1":
            pointer = pointer.right

    return decoded_string


# Test case 1
tree, encoded_data = build_huffman_tree("atharv redij")
decoded_string = decode_string(tree, encoded_data)
print(encoded_data, decoded_string, "\n")
# expected output = 1001100110110010111101111101000001010011 atharv redij

# Test case 2
tree, encoded_data = build_huffman_tree("Udacity")
decoded_string = decode_string(tree, encoded_data)
print(encoded_data, decoded_string, "\n")
# expected output = 01001110010111011100 Udacity

# Test case 3 edge case
tree, encoded_data = build_huffman_tree("")
decoded_string = decode_string(tree, encoded_data)
print(encoded_data, decoded_string, "\n")
# expected output
# Incorrect string provided for building huffman tree
# Incorrect string provided for decoding
# None None

# Test case 4 edge case
tree, encoded_data = build_huffman_tree(" ")
decoded_string = decode_string(tree, encoded_data)
print(encoded_data, decoded_string, "\n")
# expected output
# Incorrect string provided for building huffman tree
# Incorrect string provided for decoding
# None None
