from datetime import datetime
import time
formatted_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().time().strftime("%H:%M")

def sign_out(search_name):
    with open('press_attendance.txt', mode='r') as file:
        found = False
        for i in file:
            if search_name in i:
                print("Please wait...")
                time.sleep(3)
                print("Name found")
                found = True 
                with open('press_attendance_signout.txt', mode='a') as file:
                    file.write(search_name + ' has signed out '+ str(current_time) +' '+ str(formatted_date)+'\n')
                    print(search_name+ ' has signed now out '+ current_time)
                
        if not found:
            with open('casual_attendance.txt', mode='r') as file:
                found = False
                for i in file:
                    if search_name in i:
                        print("Please wait...")
                        time.sleep(3)
                        print("Name found")
                        found = True 
                        with open('casual_attendance_signout.txt', mode='a') as file:
                            file.write(search_name + ' has signed out '+ str(current_time) +' '+ str(formatted_date)+'\n')
                            print(search_name+ ' has signed now out '+ current_time)
        
        if not found:
            with open('security.txt', mode='r') as file:
                found = False
                for i in file:
                    if search_name in i:
                        print("Please wait...")
                        time.sleep(3)
                        print("Name found")
                        found = True 
                        with open('security_signout.txt', mode='a') as file:
                            file.write(search_name + ' has signed out '+ str(current_time) +' '+ str(formatted_date)+'\n')
                            print(search_name+ ' has signed now out '+ current_time)

        if not found:
            print('Are you sure you signed in today?')
            
            

