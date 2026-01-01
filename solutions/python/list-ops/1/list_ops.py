def append(list1, list2):
    """Append list2 items to list1 (modified) and return the result.
    
    Note: This function modifies list1 in place, it is unclear from requirements
    whether this is acceptable. If not, we can create a new list instead.
    """
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    """Concatenates all lists into a single new list."""
    new_list = []
    for lst in lists:
        new_list = append(new_list, lst)
    return new_list


def filter(function, list):
    """Return the list of all items matching the function predicate."""
    filtered_list = []
    for item in list:
        if function(item):
            filtered_list.append(item)
    return filtered_list


def length(list):
    """Return the length of the list"""
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    """Return a new list with function applied to each item of the input list."""
    mapped_list = []
    for item in list:
        mapped_list.append(function(item))
    return mapped_list

def foldl(function, list, initial):
    """Recursively apply function to each item and remaining list left to right,"""
    if not list:
        return initial
    return foldl(function, list[1:], function(initial, list[0])) 


def foldr(function, list, initial):
    """Recursively apply function to each last item and heading list right to left,"""
    if not list:
        return initial
    return foldr(function, list[:-1], function(initial, list[-1])) 


def reverse(list):
    """Return a new list with the items in reverse order."""
    return foldl(lambda acc, x: [x] + acc, list, [])
