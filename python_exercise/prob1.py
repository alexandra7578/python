#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

weekday=input()
vacation=input()
def sleep_in(weekday, vacation):
  if weekday==False or vacation==True:
    return True
  return False
print(sleep_in(weekday, vacation))