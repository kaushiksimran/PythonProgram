#case 1 O(n)

# def print_items(n):
#     for i in range(n):
#         print(i)
# print_items(10)

#case 2 (O(n))
# def print_items(n):
#     for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j)
# print_items(10)

#case 3 O(a+b)
# def print_items(a,b):
#     for i in range(a):
#         print(i)
#     for j in range(b):
#         print(j)
# print_items(10,30)

#case 4 O(n^2)
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)
# print_items(10)

#case 5

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 print(i,j,k)
# print_items(10)

#case 6 drop non dominant

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)
#     for k in range(n):
#         print(k)
# print_items(10)

#case 7 constant case O(1)

def add_items(n):
    return n+n+n

add_items(10)





