# 7. Recursive searching algorithm to search for a number entered by user in a list of numbers
def recursive_search(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return recursive_search(arr, target, index + 1)

if __name__ == "__main__":
    numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    target = int(input("Enter the number to search for: "))
    index = recursive_search(numbers, target)
    if index != -1:
        print(f"Number {target} found at index {index}.")
    else:
        print(f"Number {target} not found in the list.")