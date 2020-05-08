import hashlib
import time


class Block:

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode(
            'utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __init__(self, data, previous_hash=None):
        self.data = data
        self.timestamp = time.time()
        self.hash = self.calc_hash()
        self.previous_hash = previous_hash


class Blockchain:

    def __init__(self):
        self.tail = None
        self.blocks_count = 0

    def append(self, data):
        if data in [None, "", " "]:
            print("Invalid data passed")
            return

        if self.tail == None:
            self.tail = Block(data=data)
        else:
            self.tail = Block(data=data, previous_hash=self.tail)

        self.blocks_count += 1

    def search(self, data):

        if data in [None, "", " "]:
            print("Invalid data passed for search")
            return

        if self.tail == None:
            print("Block chain is empty")
            return

        head = self.tail
        while head:
            if head.data == data:
                return head
            head = head.previous_hash

        return None

    def get_size(self):
        return self.blocks_count

    def to_list(self):
        blocks = []
        if self.tail == None:
            return blocks

        head = self.tail
        while head:
            blocks.append(head.data)
            head = head.previous_hash

        return blocks


# Test cases
blockchain = Blockchain()
blockchain.append("Atharv Redij")
blockchain.append("Udacity")

# Test case 1
print(blockchain.get_size())
# expected output
# 2

# test case 2
print(blockchain.to_list())
# expected output
# ['Udacity', 'Atharv Redij']

# test case 3 edge case
blockchain.append(" ")
# expected output
# Invalid data passed

# test case 4 edge case
blockchain.search(None)
# expected output
# Invalid data passed for search
