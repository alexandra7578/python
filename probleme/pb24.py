try:
    age=int(input('Age: '))
    incom=2000
    risk=incom/age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0")
except ValueError:
    print('Invalid value')

