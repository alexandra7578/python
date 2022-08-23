#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

str=input()
n=input()

def string_times(str, n):
    cuvant=""
    for i in range(n):
        cuvant=cuvant+str
    return cuvant
print(string_times(str, int(n)))

