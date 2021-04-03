from linked_list import Node, LinkedList

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
            if item[0] == key:
                item[1] = value
                return

        list_at_array.insert(payload)
        
        return

#Function that allows you to retrieve the value based on your key
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        payload = self.array[array_index]

#Conditional statements to check the value that is stored at the relevant index based on the key
        if payload[0] == key:
            return payload[1]
        
        if payload == None:
            return None
        




# new_class = HashMap(6)
# new_class.assign('brian', 'orla')
# print(new_class.retrieve('brian'))