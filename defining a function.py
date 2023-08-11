## After defining a function, you can use it as many times as needed in your code. Using a function after defining it is referred to as calling a function. To call a function, write its name followed by parentheses.

def display_investigation_message():
    print("investigate activity")
application_status = "potential concern"
email_status = "okay"
if application_status == "potential concern":
    print("application_log:")
    display_investigation_message()
if email_status == "potential concern":
    print("email log:")
    display_investigation_message()




## the information returned from the call to remaining_login_attempts is stored in a variable called remaining_attempts.
## Then, this variable is used in a conditional that prints a "Your account is locked" message when remaining_attempts
## is less than or equal to 0.

def remaining_login_attempts(maximum_attempts, total_attempts):
    return maximum_attempts - total_attempts
remaining_attempts = remaining_login_attempts(3, 4)
if remaining_attempts <= 0:
    print("Your account is locked")