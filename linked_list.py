# using lists
# ----------------------------------
# first pointer is defined in code, next pointer is defined using the pointer[current_ptr] and so on..

Data  = ['e','b','c','','','','','','']
pointer = [-1,2,0,4,5,6,0,1,7,8]
start_ptr = 1
free_ptr = 3

# prints linked list
def linked_lst():
    current = start_ptr
    if current == -1:
        return 'empty list'
    while current!=-1:
        print(Data[current]) # print data using current pointer
        current = pointer[current] # get next pointer and store in current



# inserts at start of list
def insert_at_start(item):
    global start_ptr, free_ptr
    new_node_ptr = free_ptr
    Data[new_node_ptr] = item
    free_ptr = pointer[free_ptr]

    pointer[new_node_ptr] = start_ptr
    start_ptr = new_node_ptr


# inserts based on value
# @param item value to add to linked list
# @param start head pointer 
def insert(item, start):
    global free_ptr
    new_node = free_ptr
    Data[new_node] = item # store item in Data at index: free pointer
    free_ptr = pointer[new_node] # get next free pointer from pointer list
    current = start
    
    # while value in current node is less than item keep checking next node until
    # node greater than item found
    while Data[current] < item: 
        previous_ptr = current
        current = pointer[current]
    
    # insert item in correct place
    if current == start: # if item is being placed at head
        pointer[new_node] = start
        start = new_node
    else:
        pointer[new_node] = pointer[previous_ptr]
        pointer[previous_ptr] = new_node

