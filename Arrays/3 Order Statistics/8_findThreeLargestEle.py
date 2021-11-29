def print3largest(arr, arr_size):

    # There should be atleast three
    # elements
    if (arr_size < 3):
        print(" Invalid Input ")
        return

    third = first = second = float('-inf')

    for i in range(0, arr_size):

        # If current element is greater
        # than first
        if (arr[i] > first):

            third = second
            second = first
            first = arr[i]

        # If arr[i] is in between first
        # and second then update second
        elif (arr[i] > second):

            third = second
            second = arr[i]

        elif (arr[i] > third):
            third = arr[i]

    print("Three largest elements are",
          first, second, third)
