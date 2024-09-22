# A reminder about task and priority
task = input("Enter the task you want to do: ").proper()
task_priority = input("What is the priority of the task? (high, medium, low)").lower()
time_bound = input("Is it time bound task? (yes/no)").lower()
match time_bound:
    case "yes":
        if task_priority == "high":
            print("Reminder: ", task, " is a ", task_priority, " priority task that requires immediate attention today")
        elif task_priority == "no":
            print("Note: ", task, " is a ", task_priority, " priority task. Consider completing it when you have free time.")
        break;
    case _:
        print("Please follow the prompt's instructions")

