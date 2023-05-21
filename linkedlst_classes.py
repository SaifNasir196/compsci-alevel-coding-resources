# linked list using classes
# ----------------------------------
class node:
    def __init__(self, item, ptr):
        self.item = item
        self.ptr = ptr
    
    def __repr__(self):
        return f'{self.item}:{self.ptr}'

def create():
    global start, free, lst      
    start = -1
    free = 0
    lst = [node(0, i+1) for i in range(5)] # list of nodes
    lst[-1].ptr = -1

def printLst():
    arr = []
    cur = start
    while cur != -1:
        arr.append(lst[cur])
        cur = lst[cur].ptr
    print(arr)
    print(lst)
    
def insert(item): 
    global start, free
    # list full
    if free == -1:
        print('list full')
    else:
        newnodeptr = free
        free = lst[free].ptr
        
        lst[newnodeptr].item = item
        
     
        # check if list empty - in this case we dont need prev ptr
        if start == -1:
            start = newnodeptr
            lst[newnodeptr].ptr = -1
            return True
        
        # item needs to be added to list in correct position - look for correct position
        cur = start
        cur_item = lst[start].item
        while cur != -1 and cur_item < item: 
            prev = cur
            
            cur = lst[cur].ptr
            cur_item = lst[cur].item
        
        
        lst[prev].ptr = newnodeptr
        lst[newnodeptr].ptr = cur
        return True
    
def delete(item):
    global start
    # if the item is at the start of the list then just move the start pointer to the next node
    if item == lst[start].item:
        start = lst[start].ptr
        
    # if the item is at the end of the list then just move the end pointer to the previous node, 
    # end pointer is just -1 (null) so previous node should point at -1
    
    #if item in the middle of the list, connect prevnode and nextnode by: lst[prev].ptr = lst[cur].ptr
    cur = start
    while cur != -1:
        prev = cur
        cur = lst[cur].ptr
        if item == lst[cur].item:
            if cur ==-1:
                lst[prev].ptr = -1
            else:
                lst[prev].ptr = lst[cur].ptr

def search(item):
    cur = start
    while cur != -1:
        if lst[cur].item == item:
            return f'Item found at {cur}'    
        cur = lst[cur].ptr
    return 'Item not found'
    
    


     
create()
