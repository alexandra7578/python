#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

n = input("Introduceti numarul ")
def diff21(n):
    if int(n) <= 21:
        return 21-int(n)
    return (int(n)-21)*2
print(diff21(n))