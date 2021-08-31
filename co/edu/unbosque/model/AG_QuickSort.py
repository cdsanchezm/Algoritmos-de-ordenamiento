def quickSort(list):
    left = []
    center = []
    right = []
    if len(list) > 1:
        pivot = list[0]
        for i in list:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                center.append(i)
            elif i > pivot:
                right.append(i)
        return quickSort(left)+center+quickSort(right)
    else:
      return list
