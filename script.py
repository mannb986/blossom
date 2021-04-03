from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

#Converting key into a hash value
    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

#Compressing hash value to fit within the array size range
    def compress(self, hash_code):
        return hash_code % self.array_size

#Assign function that allows you to assign you key, value pair to the array
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for item in list_at_array:
            if key == item[0]:
                item[1] = value
                return

        list_at_array.insert(payload)

        return

#Function that allows you to retrieve the value based on your key
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        for item in list_at_index:
            if key == item[0]:
                return item[1]
        
        return None

blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('tulip'))