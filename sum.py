'''
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
'''
n = int(input("Enter the number of elements: "))
elements_list = []
for _ in range(n):
    value = int(input())
    elements_list.append(value)

elements_tuple = tuple(elements_list)
total_sum = sum(elements_tuple)
print(total_sum)