def Sort10(arr):
    arr.sort()

    result = []
    
    negatives = [x for x in arr if x < 0]
    result.extend(negatives)
    
    non_neg_odds = [x for x in arr if x >= 0 and x % 2 != 0]
    if non_neg_odds:
        result.append(non_neg_odds[0])
    
    remaining_negatives = [x for x in arr if x < 0 and x not in result]
    result.extend(remaining_negatives)

    remaining_odds = [x for x in arr if x >= 0 and x % 2 != 0 and x not in result]
    result.extend(remaining_odds)

    non_negatives = [x for x in arr if x >= 0 and x not in result]
    result.extend(non_negatives)
    
    return result

arr = [10, -1, 9, 20, -3, -8, 22, 9, 7]
sorted_arr = Sort10(arr)
print(sorted_arr)