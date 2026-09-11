def bubble_sort(arr: list) -> list:
    """
    Sorts a list of elements in ascending order using the Bubble Sort algorithm.
    Modifies the list in-place and returns it.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, array is sorted
        if not swapped:
            break
            
    return arr