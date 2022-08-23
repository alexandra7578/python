#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

a=input()
b=input()
def make_abba(a, b):
    return a + b + b + a
print(make_abba(a, b))