def init_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Creates a 2D array (matrix) based on the input rows and columns.

    Parameter(s):
    - rows (int): Specifies the rows of the 2D array to be created.
    - cols (int): Specifies the columns of the 2D array to be created.

    Returns:
    - 2D array (int): This is the 2D array that is created using the input rows and cols.
    """
    return [[None for j in range(cols)] for i in range(rows)]   #initializing a matrix


def filter_image(image: list[list[int]], kernel: list[int]) -> list[list[int]]:
    """
    Perform the convolution operation by applying the kernel over the input image.

    Parameter(s):
    - 2D array (int): This is the image on which you have to apply the kernel/filter and perform convolution. 
    - 1D array (int): The first entry in this array is the width of the kernel and the remaining entries are the values of the kernel.

    Returns:
    - 2D array (int): This is the matrix that is obtained after performing convolution.
    """
    # Extract the size of the kernel/ assuming it's square, so only one dimension is needed
    kernel_size = int(kernel[0])
    kernel_values = list(map(int, kernel[1:]))    # Extract the values of the kernel from the input list
    result = init_matrix(len(image), len(image[0]))    # Initialize a result matrix with the same dimensions as the input image, filled with None values
    offset = kernel_size // 2    # Calculate the offset to correctly position the kernel over each pixel

    # Iterate over each pixel in the input image
    for i in range(len(image)):
        for j in range(len(image[0])):
            conv_sum = 0  # Initialize the sum for the convolution operation

            # Iterate over each position in the kernel
            for ki in range(-offset, offset + 1):
                for kj in range(-offset, offset + 1):
                    ni = i + ki   # Calculate the corresponding row in the image
                    nj = j + kj      # Calculate the corresponding column in the image

                    # Check if the calculated indices are within bounds of the image
                    if 0 <= ni < len(image) and 0 <= nj < len(image[0]):
                        conv_sum += image[ni][nj] * kernel_values[(ki + offset) * kernel_size + (kj + offset)]    # Here we will perform the convolution that is multiply kernel value with corresponding image pixel value

            # Store the result of the convolution in the corresponding position of the result matrix
            result[i][j] = conv_sum

    # Return the resulting matrix after convolution
    return result

def main(file_name: str) -> list[list[int]]:
    """
    The main driver function that will run the entire program. 
    It should extract the image and the kernel from the file and pass them to filter_image(...).

    Parameter(s):
    - file_name (.txt file): Path to a text file that contains the image (2D array) and the kernel (1D array).

    Returns:
    - 2D array (int): This is the matrix that is obtained after executing filter_image(...)
    """

     # Initialize the variables, image and kernel.
    with open(file_name, 'r') as file:
        rows, cols = map(int, file.readline().strip().split())  # Read the dimensions of the image
        image = [list(map(int, file.readline().strip().split())) for _ in range(rows)]      # Read the image data into a 2D list
        kernel = file.readline().strip().split() # Read the kernel data into a list

    # Pass those variables to filter_image(...)
    return filter_image(image, kernel)

   

    
