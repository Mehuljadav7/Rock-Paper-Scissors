print("*****************************************")
print("Rock, Paper, Scissor's Account Setup File")
print("*****************************************")
while True:
    username = input("pick username: ")
    password = input("pick your password: ")
    confirm_password = input("confirm the password: ")
    if password !=  confirm_password :
        print("Passwords does not match")
    if password ==  confirm_password:
        print("Your account set up done successfully!!")
        text_file = open("accounts.txt","a")
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        break
