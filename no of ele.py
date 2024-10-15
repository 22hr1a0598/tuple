'''
 Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
input_values = input("Enter tuple elements separated by space: ")
elements_tuple = tuple(map(int, input_values.split()))
print(len(elements_tuple))
