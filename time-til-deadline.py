from datetime import datetime

user_input = input("enter your goal with a deadline seperated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_til = deadline_date - today_date

print(f"Dear user! Time remaining for your goal: {goal} is {time_til.days} days")
