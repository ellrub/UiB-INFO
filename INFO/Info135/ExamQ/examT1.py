# # Ass1.1
# # a) log 102400 / log 2 = 16.64 = 17 steps
# # b) log 480000 / log 2 = 18.87 = 19 steps

# # Ass1.2

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_list(self):
#         node = self.head
#         while node is not None:
#             print(node.data)
#             node = node.next

# node1 = Node("brunch")
# node2 = Node("bocce")
# node3 = Node("drink tea")

# todo_list = LinkedList()
# todo_list.head = node1
# node1.next = node2
# node2.next = node3

# todo_list.print_list()

# # Ass1.3
# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0
    
#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.items.pop()
    
#     def size(self):
#         return len(self.items)
    
# def reverse_list(list):
#     stack = Stack()
#     new_list = []

#     for item in list:
#         stack.push(item)

#     while not stack.is_empty():
#         new_list.append(stack.pop())

#     print(new_list)

# my_list = [1, 2, 3, 4, 5]
# reverse_list(my_list)

# # Ass2.1
# #  [ 1502, 1560, 1600, 1540, 100, 1660, 1700, 2024 ] - initial list
# # Use Selection Sort 3 times
# # [ 100, 1502, 1540, 1600, 1560, 1660, 1700, 2024 ]

# # Ass2.2
# # [ 400, 10, 210, 160, 70, 220, 280, 380, 180, 260, 540 ] - initial list
# # Use Bubble Sort 3 times
# # [ 10, 70, 160, 210, 220, 180, 260, 280, 380, 400, 540 ]

# # Ass2.3
# print("\nAssignment 2.3")
# def sort_and_rem_dup(list):
#     no_duplicates = []
#     size = len(list)
#     for pass_num in range(size):
#         minimum_index = pass_num

#         for i in range(pass_num + 1, size):
#             if list[i] < list[minimum_index]:
#                 minimum_index = i

#         temp = list[pass_num]
#         list[pass_num] = list [minimum_index]
#         list[minimum_index] = temp

#     for item in list:
#         if item not in no_duplicates:
#             no_duplicates.append(item)
#     return no_duplicates

# my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]
# new_list = sort_and_rem_dup(my_list)
# print(new_list)

# # Ass2.4
# print("\nAssignment 2.4")

# def check_palindrome(word):
#     if word == word[::-1]:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"

# result = check_palindrome('helllo')
# print(result)

# result = check_palindrome('civic')
# print(result)

def function1(n):
    count = 0
    for i in range(999):
        for j in range(n):
            count += 1
    return count
    

def function2(n):
    count = 9
    for i in range(n):
        for j in range(n):
            count += 1
    return count
    

def function3(n):
    count = 0
    for i in range(n):
        count += 1
    for j in range(n):
        count += 2
    return count
    

def function4(n):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            count += 1
    return count
    

def function5(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += i + j + k
    return count
    