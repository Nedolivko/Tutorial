class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        s = []
        count = 0
        node = self.head
        while node is not None:
            if node.value == val:
                s.append(count)
            count += 1
            node = node.next
        return s

    def delete(self, val, all=False):
        if self.head == None:
            return
        if all == True:
            while (self.head.value == val):
                self.head = self.head.next
                if self.head == None:
                    return
        else:
            if val == self.head.value:
                self.head = self.head.next
                return
        node = self.head
        while node is not None:
            if node.value == val:
                if node.next == None:
                    self.tail = node
                old.next = node.next
                node = self.head
                if all == False:
                    break
            old = node
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        self.length = 0
        if self.head != None:
            self.length += 1
            node = self.head
            while node.next != None:
                node = node.next
                self.length += 1
        return self.length

    def insert(self, afterNode, newNode):
        newnode = Node(newNode)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            return
        if afterNode == 0:
            newnode.next = self.head
            self.head = newnode
            return
        node = self.head
        count = 0
        while node != None:
            count += 1
            if count == afterNode:
                newnode.next = node.next
                node.next = newnode
                if node.next == None:
                    self.tail = node.next
                break
            node = node.next
