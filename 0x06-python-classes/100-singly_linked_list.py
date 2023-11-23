#!/usr/bin/python3

class Node:
    '''This class defines a node of a singly linked list'''

    def __init__(self, data, next_node=None):
        '''
        Initialization method for the class

        Args:
            data(int): The integer to be added to the list
            next_node: The next_node in a node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Getter method for retrieving data'''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        The setter method for inserting data to a node.

        Args:
            value(int): the integer value to be inserted'''
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        '''Getter method for retrieving a next node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        The setter method for attaching a node

        Args:
            value(node): can be none or a Node
        '''
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''A class that defines a singly linked list'''

    def __init__(self):
        '''The initialization method for the class'''
        self.__head = None

    def sorted_insert(self, value):
        '''
        A method the inserts a new node into the correct position
        in the list(increasing order).

        Args:
            value(int): the integer to be inserted to the list'''
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        '''String representation of the linked list'''
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node

        return "\n".join(result)
