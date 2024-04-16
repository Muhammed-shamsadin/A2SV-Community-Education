def countSwaps(a):
    # Write your code here
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
    firstelement = a[0]
    lastelement = a[-1]
    print(f"Array is sorted in {count} swaps.\nFirst Element: {firstelement}\nLast Element: {lastelement}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
