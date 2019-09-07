def Divisor(n, div):
    for i in range(1, n):
        if(n%i==0):
            div.append(i)

    return div