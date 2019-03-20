def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    items.sort()
    return items


def bubble_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]

    return items

def merge_sort(items):
    list1 = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            list1.append(a[0])
            a.pop(0)
        else:
            list1.append(b[0])
            b.pop(0)

    if len(a) == 0:
        list1 = list1+ b
    if len(b) == 0:
        list1 = list1 + a

    return list1


def merge_sort(items):

    len_item= len(items)
    if len_item== 1:
        return items

    midnumber = int(len_item / 2)
    item1 = merge_sort(items[:midnumber])
    item2 = merge_sort(items[midnumber:])

    return merge(item1, item2)
