'''
 Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10

'''
n = int(input("Enter the number of elements: "))
elements_list = []
for _ in range(n):
    value = int(input())
    elements_list.append(value)
elements_tuple = tuple(elements_list)
min_value = min(elements_tuple)
print(min_value)
