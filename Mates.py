def decToBin(n):
    binn = []
    while n > 0:
        binn.append(str(n % 2))
        n = n//2
    binn.reverse()
    return " ".join(binn)

def binToDec(n):
    dec = 0
    for i in range(len(n)):
        bit = int(n[i])
        power = len(n) -1 -i
        dec += bit * (2 ** power)
    return dec
