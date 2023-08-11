## If you need to iterate through a specified sequence, you should use a for loop

for i in ["elarson", "bmoreno", "tshah", "sgilmore"]:
    print(i)

computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    print(asset)

string = "security"
for character in string:
    print(character)

for i in range(0, 5, 1):
    print(i)

for i in range(5):
    print(i)




## If you want a loop to iterate based on a condition, you should use a while loop. As long as the condition is True, the loop continues, but when it evaluates to False, the while loop exits

i = 1
while i < 5:
    print(i)
    i = i + 1

login_attempts = 0
while login_attempts < 5:
    print("Login attempts:", login_attempts)
    login_attempts = login_attempts + 1

count = 0
login_status = True
while login_status == True:
    print("Try again.")
    count = count + 1
    if count == 4:
        login_status = False




## When you want to exit a for or while loop based on a particular condition in an if statement being True, you can write a conditional statement in the body of the loop and write the keyword break in the body of the conditional

computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        break
    print(asset)



## When you want to skip an iteration based on a certain condition in an if statement being True, you can add the keyword continue in the body of a conditional statement within the loop

computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue
    print(asset)
