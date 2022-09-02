phone=input(1567"Phone:")
dictionari={
    "1":"one",
    "2":"two",
    "3":"tree",
    "4":"fore",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
output=" "
for ch in phone:
    output+=dictionari.get(ch, "!") + " "
print(output)