import list_adt as listadt

def create_alien() -> dict:
    """
    Creates an 'alien' dictionary with a list to store messages.
    You can add other attributes if required

    Returns:
    A dictionary representing an 'alien' with a list to store messages:
    {
        'messages': listadt.create_list(100)    # List to store messages with a maximum capacity of 100
    }
    """
    # provide other required implementation here
    return {
        'messages': listadt.create_list(100),  #Maximum size as stated in the contstraints section of homework pdf.
        'seq_numbers': listadt.create_list(100),
        'R': None,
        'min_seq_num': None, #Minimum sequence number so far
        'max_seq_num': None #max sequence number so far
    }

def add(seq: int, msg: str, alienList: dict):
    """
    Parameters:
    - seq: The sequence number of the message.
    - msg: The message to be added.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    if alienList['R'] == None:  #Checking if it's the first message
        alienList['R'] = seq  #Seting R to the sequence number of the first message
        listadt.insert_last(msg, alienList['messages']) #Inserting message using our created listADT
        listadt.insert_last(seq, alienList['seq_numbers'])  #Inserting the sequence number at the end of the seq_numbers list
        alienList['min_seq_num'],alienList['max_seq_num'] = seq, seq # Set min and max_seq_num to the sequence number of the first message
    elif seq < alienList['min_seq_num']:  # If the sequence number is less than min_seq_num
        alienList['R'] -= 1  # Decrement R
        listadt.insert_first(msg, alienList['messages'])  
        listadt.insert_first(seq, alienList['seq_numbers']) 
        alienList['min_seq_num'] = seq  # Update min_seq_num and max would obviously remain unchanged
    elif seq > alienList['max_seq_num']:  # If the sequence number is greater than max_seq_num
        alienList['R'] += 1  #Increment R
        listadt.insert_last(msg, alienList['messages'])  
        listadt.insert_last(seq, alienList['seq_numbers'])
        alienList['max_seq_num'] = seq  # Update max_seq_num to the new sequence number
    else:
        return #Discarding otherwise

def delete(seq: int, msg: str, alienList: dict):
    
    """
    Parameters:
    - seq: The sequence number of the message to be deleted.
    - msg: The message to be deleted.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    if not listadt.is_empty(alienList['messages']) and not listadt.is_empty(alienList['seq_numbers']):
        listadt.remove_last(alienList['messages'])  # Remove the last message and its seq num from the respective lists
        listadt.remove_last(alienList['seq_numbers']) 
            

def get_messages(alienList: dict) -> str:
    """

    Parameters:
    - alienList: The 'alien' dictionary containing the messages list.

    Returns:
    A string of all messages in the conversation.
    """

    # provide implementation here
    messages = ""  # Initialize an empty string to store the messages
    for i in range(listadt.length(alienList['messages'])):  # Loop through all messages in the messages list
        messages+=' '+ listadt.get(i, alienList['messages']) # Append each message to the messages list
    return messages[1:]



def main(filename) -> str:
    """
    Reads data from a file, processes it, and returns the conversation as a list.

    Data is provided in the following format:
    There can be multiple lines in the file, each line containing an integer and an optional string separated by a space. The integer represents the sequence number of the message, and the string represents the message itself. If the string is not provided, it is assumed to be an empty string. The sequence number 0 indicates the end of the conversation.

    Process the data as follows:
    - If the sequence number is 0, stop processing the file.
    - If the sequence number is positive, add the message to the conversation.
    - If the sequence number is negative, delete the message from the conversation.
    
    Parameters:
    - filename: The name of the file to read data from.

    Returns:
    A string representing the conversation obtained from the file.
    """

    messages = create_alien()

    # Provide your implementation here

    with open(filename, 'r') as file:  # Open the file for reading
        for line in file:  # Read each line from the file
            parts = line.strip().split(' ', 1)  # Split the line into sequence number and message parts
            seq = int(parts[0])  # Convert the sequence number part to an integer
            if len(parts) > 1:
                msg = parts[1]   # Get the message part if it exists
            else:
                msg=''

            #Decision Making
            if seq == 0:  # If the sequence number is 0
                break  # Stop processing the file
            elif seq > 0:  # If the sequence number is positive
                add(seq, msg, messages)  # Add the message to the AlienADT variable: messages
            elif seq < 0:  # If the sequence number is negative then delete
                delete(seq, msg, messages)  

    #Collecting outputs that remain in the alienADT
    output = get_messages(messages)
    return output

