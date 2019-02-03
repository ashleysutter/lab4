class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        return self.sentinel.next == None

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        node = self.sentinel.next
        while True:
            if node.item == item:
                return
            elif node == self.sentinel or node.item > item: 
                new_node = Node(item)
                node.prev.next = new_node
                new_node.prev = node.prev
                node.prev = new_node
                new_node.next = node
                return
            else:
                node = node.next

    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        node = self.sentinel.next
        # node.item != None denotes we are at the sentinel node
        while node.item != None:
            if node.item == item:
               node.prev.next = node.next
               node.next.prev = node.prev
               return True
            else:
               node = node.next
        return False

    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        node = self.sentinel.next
        i = 0
        while node.item != None:
            if node.item == item:
                return i
            else:
                i+=1
                node = node.next
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0:
            raise IndexError
        node = self.sentinel.next
        for i in range(index):
            node = node.next
            if node.item == None:
                raise IndexError
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(self.sentinel.next, item)

    def search_helper(self, node, item):
        if node.item == item:
            return True
        elif node.item == None:
            return False
        else:
            return self.search_helper(node.next, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        return self.list_helper(self.sentinel.next)

    def list_helper(self, node):
        if node.item == None:
            return []
        else:
            return [node.item] + self.list_helper(node.next)

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.reverse_helper(self.sentinel.prev)

    def reverse_helper(self, node):
        if node.item == None:
            return []
        else:
            return [node.item] + self.reverse_helper(node.prev) 

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.sentinel.next)

    def size_helper(self, node):
        if node.item == None:
            return 0
        else:
            return self.size_helper(node.next) + 1
