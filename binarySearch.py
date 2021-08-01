def bubbleSort(arr,n):
    low = 0;
    high = len(arr) - 1;
    while (low<=high):
        mid = (low + high) // 2
        if (n == arr[mid]):
            return mid ## this is not value, its index.
        elif (n >= arr[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1;

def main():
    arr = [4,5,6,7,8,9,10,11,12]
    n = 11
    print(bubbleSort(arr,n))

if __name__ == "__main__":
    main();
