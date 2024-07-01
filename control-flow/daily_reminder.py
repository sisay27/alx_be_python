# daily_reminder.py

# Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the priority level (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Process the Task Based on Priority and Time Sensitivity
if time_bound == "yes":
    match priority:
        case "high":
            print(f"Reminder: {task} is {priority} Priority task ", end=" ")
        case "medium":
            print(f"Reminder: {task} is {priority} Priority task ", end=" ")
        case "low":
            print(f"Reminder: {task} is {priority} Priority task ", end=" ")

    if time_bound == "yes":
        print("that requires immediate attention today!")
elif time_bound == "no":
     match priority:
        case "high":
            print(f"Note: {task} is {priority} Priority task. Consider completing it when you have free time. ", end=" ")
        case "medium":
            print(f"Note: {task} is {priority} Priority task.Consider completing it when you have free time. ", end=" ")
        case "low":
            print(f"Note: {task} is {priority} Priority task. Consider completing it when you have free time.", end=" ")
else:
    print()