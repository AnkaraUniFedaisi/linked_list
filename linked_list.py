class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_value):
        self.next_node = new_value


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "-"
            current_node = current_node.get_next_node()
        return string_list[:-1]

    def remove_element(self, removed_element):
        current_node = self.head_node
        if current_node.get_value() == removed_element:
            self.head = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == removed_element:
                    current_node.set_next_node(next_node.get_next_node)
                    current_node = None
                else:
                    current_node = next_node


def find_nth_element(linked_list, n):
    first_pointer = linked_list.head_node
    second_pointer = None
    counter = 1

    while first_pointer:
        first_pointer = first_pointer.get_next_node()
        counter += 1
        if counter >= n + 1:
            if second_pointer is None:
                second_pointer = linked_list.head_node
            else:
                second_pointer = second_pointer.get_next_node()
    return second_pointer


def find_middle(linked_list):
    fast_pointer = linked_list.head_node
    slow_pointer = linked_list.head_node

    while fast_pointer:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()
    return slow_pointer


linkedlist = LinkedList(7)
linkedlist.insert_beginning(6)
linkedlist.insert_beginning(5)
linkedlist.insert_beginning(4)
linkedlist.insert_beginning(3)
linkedlist.insert_beginning(2)
linkedlist.insert_beginning(1)

print(linkedlist.stringify())
nth_value = find_middle(linkedlist)
print(nth_value.get_value())
