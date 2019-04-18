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
        node = self.head
        while node is not None:
            if node.value == val:
                s.append(node)
            node = node.next
        return s

    def delete(self, val, all=False):
        if self.head == None:
            return
        if all == True:
            while (self.head.value == val):
                self.head = self.head.next
                if self.head == None:
                    self.tail = None
                    return
        else:
            if val == self.head.value:
                self.head = self.head.next
                if self.head == None:
                    self.tail = None
                return
        node = self.head
        while node is not None:
            if node.value == val:
                old.next = node.next
                node = self.head
                if all == False:
                    node = self.head
                    while node is not None:
                        if node.next == None:
                            self.tail = node
                        node = node.next
                    break
            old = node
            node = node.next
        node = self.head
        while node is not None:
            if node.next == None:
                self.tail = node
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
            node = node.next
        node = self.head
        while node is not None:
            if node.next == None:
                self.tail = node
            node = node.next

    def sum_list(self, other):
        n = self.len()
        p = other.len()
        print(n,p)
        if (n == p) and (n != 0):
            node = self.head
            xnode = other.head
            t_list = LinkedList()
            while node is not None:
                t_list.add_in_tail(Node(node.value + xnode.value))
                node = node.next
                xnode = xnode.next
            t_list.print_all_nodes()
        else:
            print('Длины списков разные')
