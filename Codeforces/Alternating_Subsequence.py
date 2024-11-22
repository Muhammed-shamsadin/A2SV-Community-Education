def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        sum = 0
        i = 0
        while i < n:
            cur = a[i]
            j = i + 1
            while j < n and a[j] * a[i] > 0:
                cur = max(cur, a[j])
                j += 1
            sum += cur
            i = j
        
        print(sum)
 
if __name__ == "__main__":
    main()
