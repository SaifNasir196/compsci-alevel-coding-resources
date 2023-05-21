class node:
    def __init__(self, item, left, right) -> None:
        self.item = item
        self.left = left
        self.right = right
    def __repr__(self):
        return f'{self.item}: {self.left} - {self.right}'
        
        
lst = [node(0, i+1, -1) for i in range(6)]
root = -1
free = 0

def insert(item):
    global root, free
    # list full
    if free == -1:
        print('list full')
    
    # add node
    newnodeptr = free
    free = lst[newnodeptr].left
    
    lst[newnodeptr].item = item
    lst[newnodeptr].left = -1
    
    # list empty
    if root == -1:
        root = newnodeptr
    else:
    # middle of list
        cur = root
        while cur != -1:
            prev = cur
            
            if lst[cur].item > item:
                left = True
                cur = lst[cur].left
            else:
                cur = lst[cur].right
                left = False
        
        if left:
            lst[prev].left= newnodeptr
        else:
            lst[prev].right= newnodeptr

def preOrder(root):
    
    print(lst[root].item)
    if lst[root].left != -1:
        preOrder(lst[root].left)
        
    if lst[root].right != -1:
        preOrder(lst[root].right)
    

def InOrder(root): 
    
    if lst[root].left != -1:
        InOrder(lst[root].left)
        
    print(lst[root].item)
    
    if lst[root].right != -1:
        InOrder(lst[root].right)

    

insert(10)
insert(5)
insert(20)
insert(7)
insert(15)
InOrder(0)