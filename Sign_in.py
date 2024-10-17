from datetime import datetime
import time
formatted_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().time().strftime("%H:%M")

def sign_in(emp_name):
    emp_dept =int(input('Please select your department \nEnter (1) for Press operator\nEnter (2). for Casual worker \nEnter(3). for Security\n'))
    if emp_dept == 1:
        emp_dept = '  Press Operator  '
        with open('press_attendance.txt', mode='a') as file:
            file.write(emp_name + emp_dept + current_time +' '+ formatted_date+'\n')
            print(emp_name +' has signed in at ' + current_time)
    elif emp_dept == 2:
        emp_dept = '  Casual Worker  '
        with open('casual_attendance.txt', mode='a') as file:
            file.write(emp_name + emp_dept + current_time +' '+ formatted_date+'\n')
            print(emp_name +' has signed in at ' + current_time)
    elif emp_dept == 3:
        emp_dept = '  Security  '
        with open('security.txt', mode='a') as file:
            file.write(emp_name + emp_dept + current_time +' ' +formatted_date+'\n')
            print(emp_name +' has signed in at ' + current_time)
    else:
        print('Wrong Input')
#sign_in(emp_name =input("Please enter your name: \n"))
