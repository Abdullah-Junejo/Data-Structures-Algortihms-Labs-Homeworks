def hash_function(key, size):
    AsciTotal = 0
    if isinstance(key, int):
        return key % size
    if isinstance(key, str):
        for char in key:
            AsciTotal += ord(char)  #Add the ASCII value of each character
        return AsciTotal % size
    return -1

def collision_resolver(key, size, iteration):
    return (key + iteration) % size #Linear Probing

if __name__ == "__main__":
    print(hash_function(5,10)) # Should print 5
    print(hash_function("Hello", 10)) # Should print 0
    print(collision_resolver(hash_function("Hello", 10),10,2)) # Should print 2