# A reminder about task and priority
task = input("Enter your task:").proper()
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

customised_message1 = "that requires immediate attention today!"
customised_message2 = "Consider completing it when you have free time."
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task {customised_message}")
        else:
            print(f"Note: {task} is a {priority} priority task. {customised_message2}")
        break;
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task {customised_message}")
        else:
            print(f"Note: {task} is a {priority} priority task. {customised_message2}")
        break;
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task {customised_message}")
        else:
            print(f"Note: {task} is a {priority} priority task. {customised_message2}")
        break;
    case _:
        print("Please follow the prompt's instructions")

