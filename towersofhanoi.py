def TowerOfHanoi(n, start, aux, end):
    if n == 1:
        print("Move disk 1 from source", start, "to destination", end)
        return
    TowerOfHanoi(n - 1, start, end, aux)
    print("Move disk", n, "from source", start, "to destination", end)
    TowerOfHanoi(n - 1, aux, start, end)

# Driver code
n = 3
TowerOfHanoi(n, 'A', 'B', 'C')
