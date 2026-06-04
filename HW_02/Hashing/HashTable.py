def create_hashtable(size):
    return ([None] * size, [None] * size)

def resize_hashtable(hashtable,size,increase):
    if increase==True:
        new_size=size*2
    else:
        new_size=size//2
    is_prime=False
    while not is_prime:
        for i in range(2,new_size):
            if new_size%i==0:
                new_size+=1
                break
            if i==new_size-1:
                is_prime=True
    if new_size<7:
        new_size=7
    
    new_table = create_hashtable(new_size)
    
    # Rehash all existing elements
    for i in range(size):
        if hashtable[0][i] is not None:
            key = hashtable[0][i]
            data = hashtable[1][i]
            new_hash_value = hash_function(key, new_size)
            while new_table[0][new_hash_value] is not None:
                new_hash_value = collision_resolver(key, new_hash_value, new_size)
            new_table[0][new_hash_value] = key
            new_table[1][new_hash_value] = data
    
    return new_table, new_size

def hash_function(key, size):
    ascii_sum = sum(ord(char) for char in key)
    shifted = ascii_sum >> 4
    
    return shifted % size

def collision_resolver(key, old_address, size):
    
    offset = sum(ord(char) for char in key) // size
    return (old_address + offset) % size

def loadFactor(hashtable, size):
    # Count the number of non-empty slots
    filled_slots = 0
    for i in range(size):
        if hashtable[1][i] != None:
            filled_slots += 1
            
    # Calculate load factor as the ratio of filled slots to total size
    load_fac = filled_slots / size
    return load_fac


def put(hashtable, key, data, size):
    hash_value = hash_function(key, size)
    
    # Handle collisions
    original_hash_value = hash_value
    while hashtable[0][hash_value] is not None and hashtable[0][hash_value] != key:
        hash_value = collision_resolver(key, hash_value, size)
        if hash_value == original_hash_value:
            raise Exception("Hash table is full or collision resolution failed")
    
    hashtable[0][hash_value] = key
    hashtable[1][hash_value] = data
    
    # Check load factor and resize if needed
    load_fac = loadFactor(hashtable, size)
    if load_fac > 0.75:
        hashtable, size = resize_hashtable(hashtable, size, True)
    elif load_fac < 0.3:
        hashtable, size = resize_hashtable(hashtable, size, False)
    
    return hashtable, size

def Update(hashtable, key, columnName, data, size, collision_path, opNumber):
    index = hash_function(key, size)
    path = []  # To track collision path for this operation

    while True:
        if hashtable[0][index] is None:
            # Stop if the slot is empty and key is not found
            break
        if hashtable[0][index] == key:
            # Update the specified column
            hashtable[1][index][columnName] = data
            path.append(index)  # Add the index where the update succeeds
            break
        if index not in path:
            path.append(index)  # Add the index where a collision occurs
        index = collision_resolver(key, index, size)

    collision_path[opNumber] = path

def get(hashtable, key, size, collision_path, opNumber):
    index = hash_function(key, size)
    path = []  # To track collision path for this operation

    while True:
        if hashtable[0][index] is None:
            # Item not found
            print("Item not found")
            break
        if hashtable[0][index] == key:
            # Print the student record
            print(hashtable[1][index])
            path.append(index)  # Add the index where the item is found
            break
        if index not in path:
            path.append(index)  # Add the index where a collision occurs
        index = collision_resolver(key, index, size)

    collision_path[opNumber] = path

def delete(hashtable, key, size, collision_path, opNumber):
    load_fac = loadFactor(hashtable, size)
        
    if load_fac < 0.3:
        hashtable, size = resize_hashtable(hashtable, size, False)
    index = hash_function(key, size)
    path = []  # To track collision path for this operation
    
    while True:
        
        
        if hashtable[0][index] == key or hashtable[0][index]=='#':
            # Mark the slot with a tombstone and delete the key
            hashtable[0][index] = '#'
            hashtable[1][index] = None
            if index not in path:
                path.append(index)
            break
        
    # Check load factor and resize if needed
        if index not in path:
            path.append(index)
        load_fac = loadFactor(hashtable, size)
        if load_fac < 0.3:
            hashtable, size = resize_hashtable(hashtable, size, False)
        index = collision_resolver(key, index, size)

    collision_path[opNumber] = path
    





        
        

    




    

















        

        
        


