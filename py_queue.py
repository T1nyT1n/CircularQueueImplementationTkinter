from dataclasses import dataclass
from typing import Optional

@dataclass
class ListItem:
    data: int
    next: Optional["ListItem"] = None

head: Optional["ListItem"] = None
tail: Optional["ListItem"] = None
count = 0

def EmptyQueue() -> bool:
    if tail == None:
        return True
    else:
        return False
    
def ReadElement():
    if head != None:
        return head.data
    else:
        return "Пусто!"

def PushElement(data_to_insert: int):
    global head, tail, count
    new_list_item = ListItem(data=data_to_insert, next=head)
    if EmptyQueue():
        new_list_item.next = new_list_item
        tail = new_list_item
        head = new_list_item
    else:
        tail.next = new_list_item
        tail = new_list_item
    count += 1
    
def PopElement() -> int:
    global head, tail, count
    if EmptyQueue() != True:
        temp = head
        """
        Важно использовать is, а не ==, чтобы не возникало бесконечной 
        рекурсии при проверке next, ведь очередь цикличная.
        """
        if tail is head:
            head = None
            tail = None
        else:
            head = head.next
            tail.next = head
        int_to_return = temp.data
        del temp
        count -= 1
        return int_to_return
    else:
        return -1

def ClearQueue() -> int:
    if EmptyQueue() != True:
        elements_count = 0
        while not EmptyQueue():
            PopElement()
            elements_count += 1
        return elements_count
    else:
        return -1

def ShowAllElements():
    global head
    elements_string = ""
    if EmptyQueue() != True:
        current_element = head
        while current_element.next is not head:
            elements_string += str(current_element.data)
            elements_string += ", "
            current_element = current_element.next
        elements_string += str(current_element.data)
        return elements_string
    else:
        return -1

def RemoveElementsByCondition(condition: int, num: int):
    if not EmptyQueue():
        for i in range(count):
            current_data = int(ReadElement())
            PopElement()
            if (condition == 0) and (current_data >= num):
                PushElement(current_data)
            elif (condition == 1) and (current_data <= num):
                PushElement(current_data)
            elif (condition == 2) and (current_data != num):
                PushElement(current_data)
    else:
        return -1