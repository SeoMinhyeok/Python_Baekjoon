div = []  # divisor
dsum = 0 # divisors sum

def Divisors_sum(div, dsum):
    for x in range(len(div)):
        dsum += div[x]

    return dsum