# Worst case if the list in reverse order O(n^2)
# best case if the list is already sorted so no shift/swap O(n)
def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):  # has to start at 1 in order to compare to value at 0
        key = list_to_sort[i]
        j = i - 1

        # while: J continuously getting smaller but always above 0. key is being compared to every value down list
        while j >= 0 and key < list_to_sort[j]:
            list_to_sort[j + 1] = list_to_sort[j]  # shifts larger(j) over (j+1)
            j -= 1  # decrements j to keep moving down the list
        list_to_sort[j + 1] = key  # new key is set to the next in the list after traversing down


# O(n logn) time
# O(n) space
def merge(a, start, mid, end):
    left = a[start:mid]
    right = a[mid:end]
    i, j, k = 0, 0, start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        a[k] = right[j]
        k += 1
        j += 1


def merge_sort(list_to_sort):
    recursive_merge_sort(list_to_sort, 0, len(list_to_sort))


def recursive_merge_sort(list_to_sort, left, right):
    if left + 1 < right:
        middle = (left + right) // 2
        recursive_merge_sort(list_to_sort, left, middle)
        recursive_merge_sort(list_to_sort, middle, right)
        merge(list_to_sort, left, middle, right)


# *TEST*
x = [3, 635, 636, 458, 23, 6, 2, 534, 675, 87, 23543, 24, 24, 87, 355, 6255]
y = [53,734,3,87,256,908,2,45765,2,52,76,48,265,643,54,7331]

print(x)
print(y)
print()
merge_sort(x)
insertion_sort(y)
print(x)
print(y)
