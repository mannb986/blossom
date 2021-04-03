class HashMap():
    def __init__(self, size):
        self.array_size = size
        self.array = [None for item in range(size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        self.array[array_index] = [key, value]
        return

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        payload = self.array[array_index][1]
        return payload




# new_class = HashMap(6)
# new_class.assign('brian', 'orla')
# print(new_class.retrieve('brian'))