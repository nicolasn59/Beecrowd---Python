while True:
    testes = int(input())

    if testes == 0:
        break

    m, n = map(int, input().split())

    for _ in range(testes):
        x, y = map(int, input().split())

        if x == m or y == n:
            print('divisa')
        else:
            if x < m and y > n:
                print('NO')
            elif x > m and y > n:
                print('NE')
            elif x > m and y < n:
                print('SE')
            else:
                print('SO')
