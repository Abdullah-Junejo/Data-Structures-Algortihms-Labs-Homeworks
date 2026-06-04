from Question3 import *

def delete(hashtable, key, size):
    initial_hash_value = hash_function(key, size)

    if hashtable[0][initial_hash_value] != key:
        #Resolve collision using linear probing
        iteration = 0
        new_hash = initial_hash_value
        while hashtable[0][new_hash] is not None and hashtable[0][new_hash] != key:
            iteration += 1
            new_hash = collision_resolver(initial_hash_value, size, iteration)
            if new_hash == initial_hash_value:
                return  None 

        if hashtable[0][new_hash] == key:
            hashtable[0][new_hash] = "#"
            hashtable[1][new_hash] = "#"
    else:
        hashtable[0][initial_hash_value] = "#"
        hashtable[1][initial_hash_value] = "#"

if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    delete(H,5,10)
    print(H)
    # Should print ([None, None, None, None, None, '#', None, None, None, None], [None, None, None, None, None, '#', None, None, None, None])