# Decrypts the data using the logic of the Karatsuba algorithm.
# Args:
#   data: List of list consisting leaves
# Returns:
#   A tuple containing the original two numbers.
def reverse_karatsuba(data) -> tuple:
    if isinstance(data, tuple):
        return data
    

    #Recursively call reverse_karatsuba on the three sub-trees representing z0, z1, and z2
    z0 = reverse_karatsuba(data[0])
    z1 = reverse_karatsuba(data[1])
    z2 = reverse_karatsuba(data[2])

    # Calculate the base B and m (half the number of digits in z2)
    B = 10  # Base of the number system
    # Half the number of digits in z2
    m = len(str(z0[0]))
    q = len(str(z0[1]))
    # Calculate the original numbers (x, y) using the reverse Karatsuba formula
    x = z2[0] * B**m + z0[0]
    y = z2[1] * B**q + z0[1]

    return x, y  #returning as a tuple


# This function reads data from a specified file and decrypt data using the logic of the Karatsuba algorithm.
# Args:
#   filename: The name of the file containing input data.
# Returns:
#   A list of tuples, each tuple representing coordinates (x, y).

def main(filename) -> list[tuple[int, int]]:  # Call main function with the filename to get the decrypted coordinates
    filename = "input_decrypt.txt"
    with open(filename, mode='r') as file:
        N = int(file.readline().strip())  # Read the number of trees
        trees = [eval(file.readline().strip()) for _ in range(N)]  # Read and evaluate each tree

        coordinates = []   #empty list
        for tree in trees:
            x, y = reverse_karatsuba(tree)   #reverse_karatsuba formula applied on x, y
            coordinates.append((x, y))   #appended in the list

        return coordinates    #return the list with the appended tuples















