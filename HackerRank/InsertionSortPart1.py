def insertionSort1(n, arr):
    # Write your code here
    for i in range(n - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            temp = arr[i]
            arr[i] = arr[i - 1]
            print(*arr)
            arr[i - 1] = temp
        else:
            break
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
