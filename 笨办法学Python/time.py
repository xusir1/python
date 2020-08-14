def check_fermat(a,b,c,n):
    if n > 2 and a**n+b**n==c**n:
        return ("it's impossable")
    else:
        return ("it's ture")

a = int(input("insert you mind number calld a "))
b = int(input("insert you mind number calld b"))
c = int(input("insert you mind number calld c"))
n = int(input("insert you mind number calld n"))

print(check_fermat(a,b,c,n))