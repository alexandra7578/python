#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

a=input()
b=input()
sum=0
def sum_double(a, b):
    sum= a + b
    if a!=b:
        return sum
    return sum *  2
print(sum_double(int(a), int(b)))