def IsEmpty(queue):
    return queue == []

def DeQueue(queue):
    if IsEmpty(queue):
        return None
    temp_queue = []
    min_priority_item = queue[0]
    
    #Find an lower priority item if it exists
    for item in queue:
        if item[1] < min_priority_item[1]:
            min_priority_item = item

    #Transfer elements to the temporary queue, except the min priority item
    while queue:
        item = queue.pop(0)
        if item != min_priority_item:
            temp_queue.append(item)
    
    #Transfer elements back to the main queue.
    while temp_queue:
        queue.append(temp_queue.pop(0))
        
    #The reason i did this is because queue traditionaly can only use primitive opertaions like pop. it can't remove from between the array.
    return min_priority_item[0]


def EnQueue(queue, item, priority):
    count = 0
    for i, _ in queue:
        if i == item:
            queue[count] = item, priority
            return None
        count += 1
    queue.append((item, priority))

if __name__ == "__main__":
    queue = []
    EnQueue(queue,'A',1)
    EnQueue(queue,'B',2)
    EnQueue(queue,'C',3)
    EnQueue(queue,'D',4)
    EnQueue(queue,'E',5)
    EnQueue(queue,'F',6)
    EnQueue(queue,'G',7)
    print(queue)
    print(DeQueue(queue))
    print(queue)


    

