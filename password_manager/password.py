

pwd=input("What is the master password? ")
def view():

    with open('password.txt', 'r') as f:
        for line in f.readline():
            data=line.rsplit()
            user, passw=data.split("|")
            print("user: ", user, "| Password:", passw)


def add():
    name=input("Account name: ")
    pwd=input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name+"|"+pwd+"\n")

while True:
    mode = input("Would yo like to add a new password or view existing ones(view, add), press q to quit? ").lower()
    if mode=='q':
        break

    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode.")
        continue