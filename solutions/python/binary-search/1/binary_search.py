def find(search_list, value):

    s = search_list
    def rec_find(start, end):
        if end <= start:
            raise ValueError("value not in array")
        # Invariant: start < end, if value exists start <= pos[value] < end
        mid = (start + end) // 2
        if value > s[mid]:
            return rec_find(mid+1, end)
        if value < s[mid]:
            return rec_find(start, mid)
        return mid
        
    return rec_find(0, len(search_list))
