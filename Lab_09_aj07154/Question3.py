from Question1 import *
from Question2 import *

def put(hashtable, key, data, size):
    initial_hash_value = hash_function(key, size)
    
    if hashtable[0][initial_hash_value] == None:
        #Place the key and value in the hashtable at the hash value index if it is empty
        hashtable[0][initial_hash_value] = key
        hashtable[1][initial_hash_value] = data
    else:
        if hashtable[0][initial_hash_value] == key:
            #If the key already exists, insert the value
            hashtable[1][initial_hash_value] = data
        else:
            #Resolve collision using linear probing
            iteration = 0
            new_hash = initial_hash_value
            while hashtable[0][new_hash] != None and hashtable[0][new_hash] != key:
                iteration += 1
                new_hash = collision_resolver(initial_hash_value, size, iteration)
            #Repeating the initial if conditions essentially after finding the correct index
            if hashtable[0][new_hash] == None:
                # Place the key and value in the hashtable at the new hash value index if it is empty
                hashtable[0][new_hash] = key
                hashtable[1][new_hash] = data
            elif hashtable[0][new_hash] == key:
                # If the key already exists at the new hash value index, update the value
                hashtable[1][new_hash] = data

def get(hashtable, key, size):
    initial_hash_value = hash_function(key, size)
    iteration = 0
    new_hash = initial_hash_value
    while hashtable[0][new_hash] != None:
        if hashtable[0][new_hash] == key and hashtable[0][new_hash] != "#":
            return hashtable[1][new_hash]
        else:
            iteration += 1
            new_hash = collision_resolver(initial_hash_value, size, iteration)
            if new_hash == initial_hash_value:  #When Index has circled back! It means it does not exist
                break
    return None

if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    print(get(H,5,10)) # Should print 3