gro={}

try:
    while True:
        item=input().upper()

        if item in gro:
            gro[item]=gro[item]+1

        else:
            gro[item]=1


except EOFError:
    for i in sorted(gro):
        print(f"{gro[i]} {i}")


       