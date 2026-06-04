from list_adt import *

# Create a basic queue
def create_queue(size: int) -> dict:
    """
    Description: Creates and initializes a basic queue with a specified size.
    Parameters: size - an integer representing the size of the queue.
    Return: A dictionary representing the initialized queue.
    """
    return create_list(size)

# Create a priority queue
def create_priority_queue(size: int) -> dict:
    """
    Description: Creates and initializes a priority queue with a specified size.
                 Each element in the queue is a tuple consisting of data and priority.
    Parameters: size - an integer representing the size of the priority queue.
    Return: A dictionary representing the initialized priority queue.
    """
    priority_queue = create_list(size)
    priority_queue['data'] = [(None, float('inf'))] * size
    return priority_queue

# Check if the queue is full
def is_full(queue: dict) -> bool:
    """
    Description: Checks if the given queue is full (reached its maximum capacity).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is full, False otherwise.
    """
    if queue['n'] == queue['size']:
        return True
    return False


# Check if the queue is empty
def is_empty(queue: dict) -> bool:
    """
    Description: Checks if the given queue is empty (contains no elements).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is empty, False otherwise.
    """
    if queue['n'] == 0:
        return True
    return False


# Add an element to the rear of the queue
def enqueue(queue: dict, item):
    """
    Description: Adds an element with the value 'val' to the rear of the queue.
    Parameters: queue - a dictionary representing the queue, val - the value to be added to the queue.
    """
    if is_full(queue):
        print("Queue is full")
        return
    insert_last(item, queue)

# Remove and return the element from the front of the queue
def dequeue(queue: dict) :
    """
    Description: Removes and returns the element from the front of the queue.
    Parameters: queue - a dictionary representing the queue.
    Return: The element from the front of the queue.
    """
    if is_empty(queue):
        print("Queue is empty")
        return
    return remove_first(queue)

# Return the element at the front of the queue without removing it
def peek(queue: dict):
    """
    Description: Returns the element at the front of the queue without removing it.
    Parameters: queue - a dictionary representing the queue.
    Return: The element at the front of the queue.
    """
    if is_empty(queue):
        print("Queue is empty")
        return
    return get_first(queue)

# Add an element with priority to the priority queue
def enqueue_priority(priority_queue: dict, item, priority: int):
    """
    Description: Adds an element with the value 'val' and the specified priority to the priority queue.
    Parameters: queue - a dictionary representing the priority queue, val - the value to be added to the queue,
                priority - the priority of the element.
    """
    if is_full(priority_queue):
        print("Queue is full")
        return
    insert_last((item, priority), priority_queue)

# Remove and return the element with the minimum priority from the priority queue
def dequeue_min_priority(priority_queue: dict):
    """
    Description: Removes and returns the element with the minimum priority from the priority queue.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
def dequeue_min_priority(priority_queue: dict):
    if is_empty(priority_queue):
        print("Queue is empty")
        return
    
    min_priority_index = priority_queue['i'] #Starting point

    #Finding min_priority_index
    for j in range(priority_queue['n']):
        index = (priority_queue['i'] + j) % priority_queue['size']
        if priority_queue['data'][index][1] < priority_queue['data'][min_priority_index][1]:
            min_priority_index = index
    
    item = priority_queue['data'][min_priority_index] #Min priority item

    #Calculating last index as per circular nature
    last_index = (priority_queue['i'] + priority_queue['n'] - 1) % priority_queue['size']
    priority_queue['data'][min_priority_index] = priority_queue['data'][last_index] #Saving the last index' value
    priority_queue['data'][last_index] = (None, float('inf')) #Reseting the last index
    priority_queue['n'] -= 1  #Decrementing number of elements
    
    #resetting queue start index if needed
    if priority_queue['n'] == 0:
        priority_queue['i'] = 0
    return item

# Return the element with the minimum priority from the priority queue without removing it
def peek_min_priority(priority_queue: dict):
    """
    Description: Returns the element with the minimum priority from the priority queue without removing it.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    if is_empty(priority_queue):
        print("Queue is empty")
        return
    
    min_priority_index = priority_queue['i']
    #Finding min priority index
    for j in range(priority_queue['n']):
        index = (priority_queue['i'] + j) % priority_queue['size']
        if priority_queue['data'][index][1] < priority_queue['data'][min_priority_index][1]:
            min_priority_index = index

    #Returning that item
    return priority_queue['data'][min_priority_index]

def CallSimulator(callQueue, agentQueue) -> list:
    currentTime = 0
    callLog = []

    while not is_empty(callQueue) or any(agent[1] != float('inf') for agent in agentQueue['data']):
        # Debug: Print current time and the state of the queues
        print(f"Current Time: {currentTime}")
        print(f"Call Queue: {callQueue['data']}")
        print(f"Agent Queue: {agentQueue['data']}")

        # Update agent priorities as they become available
        for _ in range(agentQueue['n']):
            agent = peek_min_priority(agentQueue)
            agent_name, agent_priority = agent
            if agent_priority <= currentTime:
                dequeue_min_priority(agentQueue)
                enqueue_priority(agentQueue, agent_name, float('inf'))

                # Debug: Print agent availability details
                print(f"Agent {agent_name} becomes available at time {currentTime}")
            else:
                break

        # Process any call whose start time is less than or equal to current time
        processed_call = False
        if not is_empty(callQueue):
            for _ in range(callQueue['n']):
                call = peek(callQueue)
                caller_name, call_start, call_duration = call

                if call_start <= currentTime:
                    if not is_empty(agentQueue):
                        call = dequeue(callQueue)
                        agent = dequeue_min_priority(agentQueue)
                        agent_name, _ = agent

                        call_end = currentTime + call_duration
                        enqueue_priority(agentQueue, agent_name, call_end)

                        wait_time = currentTime - call_start
                        callLog.append((caller_name, currentTime, call_end, wait_time))

                        # Debug: Print call assignment details
                        print(f"Assigned Call: {caller_name}, Start Time: {currentTime}, End Time: {call_end}, Wait Time: {wait_time}")

                        processed_call = True
                        break
                else:
                    break

        if not processed_call:
            currentTime += 1

    return callLog





def main(filename) -> list:
    """
    Description: Main function to read input data from a file, initialize agent and call queues, simulate call processing using CallSimulator, and return the call log data.
    Parameters: filename - the name of the file containing input data.
    Return: A list representing the call log data.
    """
    
    # Read input data from the file
    # First line contains the list of agents separated by spaces 
    # Second line contains the number of calls to be processed
    # Populate the call queue with call details from the remaining lines contain the call details (start time, caller name, call duration) separated by spaces

    # provide your implementation here 
    with open(filename, 'r') as file:
        lines = file.readlines()

    # First line contains the list of agents separated by spaces
    agents = lines[0].strip().split()
    agentQueue = create_priority_queue(len(agents))
    for agent in agents:
        enqueue_priority(agentQueue, agent, float('inf'))

    # Second line contains the number of calls to be processed
    number_of_calls = int(lines[1].strip())
    callQueue = create_queue(number_of_calls)

    # Populate the call queue with call details from the remaining lines
    for line in lines[2:]:
        call_details = line.strip().split()
        call_start = int(call_details[0])
        caller_name = call_details[1]
        call_duration = int(call_details[2])
        enqueue(callQueue, (caller_name, call_start, call_duration))

    # Simulate call processing using CallSimulator
    call_log = CallSimulator(callQueue, agentQueue)

    # Return the call log data as a list
    return call_log

filename = 'inputs/callcenter01.txt'
call_log = main(filename)
print(call_log)

