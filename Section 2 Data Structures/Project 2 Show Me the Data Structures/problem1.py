from collections import OrderedDict


class LRU_Cache():

    def __init__(self, capacity):
        # Initialize class variables
        if capacity != None and capacity > 0:
            self.capacity = capacity
            self.cache = OrderedDict()
        else:
            print("Invalid cache capacity. Must be positive integer")
            return None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        # removing old one and adding so that it becomes recently accessed
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value

        else:
            # Add to cache as there is still space on cache
            if len(self.cache) < self.capacity:
                self.cache[key] = value

            else:
                # No space in cache
                # remove first element from cache i.e least recently used
                self.cache.popitem(last=False)
                self.cache[key] = value


# Test cases

# Test case 1
cache = LRU_Cache(4)

cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)

print(cache.get(2))
print(cache.get(9))

cache.set(5, 5)
cache.set(6, 6)

print(cache.get(3))

# expected output
# 2
# -1
# -1


# Test case 2
cache = LRU_Cache(3)

cache.set(1, 1)
cache.set(2, 2)
cache.set(4, 4)

print(cache.get(2))
cache.set(5, 5)
cache.set(6, 6)

print(cache.get(4))

# expected output
# 2
# -1

# Test case 3 edge case
cache = LRU_Cache(0)

# expected output
# Invalid cache capacity. Must be positive integer

# Test case 4 edge case
cache = LRU_Cache(None)

# expected output
# Invalid cache capacity. Must be positive integer
