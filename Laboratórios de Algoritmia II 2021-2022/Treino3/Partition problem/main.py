# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.e


def findpartition(array,N ):
    for i in range(0,N):
        sum+=array[i]
    if sum%2 != 0:
        return false
    return equalsubset(array, N, sum // 2 )


def equalsubset(array, N,sum):
    if sum == 0:
        return True
    if N == 0 and sum != 0:
        return False

    if array[n-1] > sum:
        return equalsubset(array, N-1,sum)

    return equalsubset(array,N-1,sum) or equalsubset(array, N-1, sum-array[N-1])


def main():

    return 1+2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
examples
arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.

'''