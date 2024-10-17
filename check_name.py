import Main
def name_check(emp_name):
    with open("press_attendance.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]  # Read and strip spaces from each line
        # Check if the emp_name matches the first word in any line
        if emp_name in [line.split()[0] for line in lines]:
            print(emp_name + " has already signed in")
        
        

#name_check(emp_name=input("Please enter your name: \n"))
