def negative_count(a, r, c):
    """takes in a 2-dimensional array and returns the number of negative numbers
    a = array
    r = number of rows in an array
    c = number of columns of array"""

    count = 0

    # Start at top left corner of array & count the number of negative numbers
    for i in range(r):
        for j in range(c):

            if a[i][j] < 0:
                count += 1

            else:
                # no more negative numbers in this row
                break
    return count


array = [
      [-4,-3,-1,1],
      [-2,-2,1,2],
      [-1, 1,2,3],
      [1,2,4,5]
    ]




print(negative_count(array,4,4))
