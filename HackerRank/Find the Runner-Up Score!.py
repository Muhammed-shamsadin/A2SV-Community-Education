if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    k = set(arr)
    k.remove(max(k))
    print(max(k))
