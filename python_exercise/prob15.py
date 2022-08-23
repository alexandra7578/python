#Given a non-empty string like "Code" return a string like "CCoCodCode".

str=input()
def string_splosion(str):
    rezultat=""
    for i in range(len(str)):
        rezultat=rezultat+str[:i+1]
    return rezultat
print(string_splosion(str))