weight=int(input("weight: "))
what=input('(L)bs or (K)g ')
if what=='L' or what=='l':
    conv=weight *0.45
    print(f"you are {conv} kilos")
else:
    con=weight/0.45
    print(f"you are {con} pounds")