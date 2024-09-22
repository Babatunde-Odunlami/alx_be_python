# A reminder about task and priority
task = input("Enter your task:").proper()
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f "Reminder: {task} is a {priority} priority task that requires immediate attention today")
        else:
            print(f "Note: {task} is a {_priority} priority task. Consider completing it when you have free time.")
        break;
    case _:
        print("Please follow the prompt's instructions")

