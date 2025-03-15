while True:
    n = int(input())

    if n == -1:
        break

    l = []

    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    if n == sum(l):
        p = ""
        for j in range(len(l)):
            p += str(l[j])
            if j < len(l) - 1:
                p += " + "
        print(n, "=", p)
    else:
        print(n, "is NOT perfect.")