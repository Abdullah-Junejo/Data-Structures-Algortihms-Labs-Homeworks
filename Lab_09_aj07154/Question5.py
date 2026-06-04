from Question4 import *

def main(to_put, to_delete, to_get, size):
    hashtable = create_hashtable(size)
    for key, value in to_put:
        put(hashtable, key, value, size)
    for key in to_delete:
        delete(hashtable, key, size)
    retrieved_values = []
    for key in to_get:
        value = get(hashtable, key, size)
        if value != None:
            retrieved_values.append(value)
    return tuple((retrieved_values, hashtable))

if __name__ == "__main__":
    size = 5
    to_put = [(1 ,2) ,(" key "," value")]
    to_delete = [1]
    to_get = [" key "]
    print(main (to_put , to_delete , to_get , size))
    # Shoud print ([' value '], ([None, '#', None, ' key ', None], [None, '#', None, ' value ', None]))