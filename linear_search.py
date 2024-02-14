def linear_search(value_to_find, array_to_search_through):
    index_counter = 0
    sort = sorted(array_to_search_through)
    print(sort)
    left=0
    right = len(sort)-1
    while left<=right:
        mid = (left+right) // 2
        
        if sort[mid]==value_to_find
            if sort[mid-1] != value_to_find:
                return mid
            elif sort[mid-1] == value_to_find:
                right = mid
        elif sort[mid] < value_to_find:
            left = mid+1
        elif sort[mid] > value_to_find:
            right = mid-1
    return -1

print(linear_search("a", ["b", "a", "n", "a", "n", "a", "s"]))

    # for letter in array_to_search_through:
    #     if letter == value_to_find:
    #         return index_counter
    #     index_counter += 1
    # # your code here
    # pass




def linear_search_global(value_to_find, array_to_search_through):
    index_counter = 0
    output = []
    for letter in array_to_search_through:
        if letter == value_to_find:
            output.append(index_counter)
        index_counter += 1
    return output


print(linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]))