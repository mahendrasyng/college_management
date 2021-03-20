import mysql.connector as mysql
connector_object = mysql.connect(host="localhost",user="root",password="",database="college")
cursor_object = connector_object.cursor(buffered=True) #for running multiple quries

def admin_session():
    while 1:
        print("")
        print("Admin menu")
        print("1. Register new student")
        print("2. Register new Teacher")
        print("3. Delete existing student")
        print("4. Delete Existing Teacher")
        print("5. Logout")

        user_option = input(str("option : "))
        if user_option == "1":
            print("")
            print("Register New Student")
            username = input(str("student username : "))
            password = input(str("student password : "))
            query_vals = (username,password)
            cursor_object.execute("Insert into user(username,password,privilege) Values (%s,%s.'student')",query_vals)
            connector_object.commit()
            print(username + "has been registered as a student")


def auth_admin():
    print("")
    print("Admin login")
    print("")
    username = input(str("username : "))
    password =input(str("password : "))
    if username == "Admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("login details not recognised")
def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as a student  ")
        print("1. Login as a Teacher ")
        print("1. Login as a Admin ")
        user_option = input(str("option : "))
        if user_option == "1":
            print("Student login")
        elif user_option == "2":
            print("Teacher login")
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid  option was selected")

            main()
