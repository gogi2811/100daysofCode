# # Given the size and the elements of array A, print all the elements in reverse order.
# #
# # Input:
# # First line of input contains, N - size of the array.
# # Following N lines, each contains one integer, i{th} element of the array i.e. A[i].
# #
# # Output:
# Print all the elements of the array in reverse order, each element in a new line.

# INPUT      OUTPUT
# 5  array size
# 4           9
# 15          15
# 7           7
# 12          12
# 9            4

array = list(map(int, input().split()))


def reverse():
    for i in array[::-1]:
        print(i)

reverse()