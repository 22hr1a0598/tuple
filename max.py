'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
n = int(input("Enter the number of elements: "))
elements_list = []
for _ in range(n):
    value = int(input())
    elements_list.append(value)
elements_tuple = tuple(elements_list)
max_value = max(elements_tuple)
print(max_value)
