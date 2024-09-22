# A reminder about task and priority
task = input("Enter your task:").proper()
task_priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()
match time_bound:
    case "yes":
        if task_priority == "high":
            print(f "Reminder: {task} is a {task_priority} priority task that requires immediate attention today")
        elif task_priority == "no":
            print(f "Note: {task} is a {task_priority} priority task. Consider completing it when you have free time.")
        break;
    case _:
        print("Please follow the prompt's instructions")

