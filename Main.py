import Sign_in
import Sign_out


while True:
    try:
        choice = int(input('Welcome to Plattenberg Press \nPRESS 1 TO SIGN-IN\nPRESS 2 TO SIGN-OUT\nPRESS 0 TO EXIT\n'))
        if choice == 1:
            files_to_check =['press_attendance.txt', 'casual_attendance.txt', 'security.txt']
            emp_name = input("Please enterrrr your name: \n").strip()
            for file_name in files_to_check:
                with open(file_name, "r") as file:
                    lines = [line.strip() for line in file.readlines()]
            if emp_name in [line.split()[0] for line in lines]:
                        print(emp_name + " has already signed in")
            if emp_name not in files_to_check:
                Sign_in.sign_in(emp_name)
                        
        elif choice == 2:
            search_name = input('Enter name: \n').strip()
            with open("security_signout.txt", "r") as file:
                lines = [line.strip() for line in file.readlines()]
                if search_name in [line.split()[0] for line in lines]:
                    print(search_name + " has already signed in")
                else:
                    Sign_in.sign_in(emp_name)
            with open("casual_attendance_signout.txt", "r") as file:
                lines = [line.strip() for line in file.readlines()]
                if search_name in [line.split()[0] for line in lines]:
                    print(search_name + " has already signed in")
                else:
                    Sign_in.sign_in(emp_name)
            with open("security_signout.txt", "r") as file:
                lines = [line.strip() for line in file.readlines()]
                if search_name in [line.split()[0] for line in lines]:
                    print(search_name + " has already signed in")
                else:
                    Sign_out.sign_out(search_name)
        elif choice == 0:
            print('Exiting the system. Goodbye!')
            break  # Exit the loop when the user inputs 0
        else:
            print('Error, please try again and enter the right value')
            
    except ValueError:
        print('Invalid input. Please enter a number (0, 1, or 2).')
