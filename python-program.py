import datetime
import csv
import random

def add_task(tasks, title, due_date):
    """
    Add a new task to the task list.
    Returns the task ID of the newly added task.
    """
    task_id = random.randint(1000, 9999)
    task = {
        'id': task_id,
        'title': title,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    return task_id

def list_tasks(tasks):
    """
    Return a formatted list of all tasks.
    """
    if not tasks:
        return "No tasks found."
    
    task_list = []
    for task in tasks:
        status = "✓" if task['completed'] else " "
        task_list.append(f"[{status}] {task['id']}: {task['title']} (Due: {task['due_date']})")
    return "\n".join(task_list)

def mark_complete(tasks, task_id):
    """
    Mark a task as complete by its ID.
    Returns True if successful, False if task not found.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return True
    return False

def save_to_csv(tasks, filename='tasks.csv'):
    """
    Save tasks to a CSV file.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'due_date', 'completed'])
        writer.writeheader()
        writer.writerows(tasks)

def load_from_csv(filename='tasks.csv'):
    """
    Load tasks from a CSV file.
    Returns a list of tasks.
    """
    tasks = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['completed'] = row['completed'].lower() == 'true'
                tasks.append(row)
    except FileNotFoundError:
        pass
    return tasks

def main():
    """
    Main function to run the task management system.
    """
    tasks = load_from_csv()
    
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Complete")
        print("4. Save and Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_id = add_task(tasks, title, due_date)
            print(f"Task added with ID: {task_id}")
            
        elif choice == '2':
            print("\nCurrent Tasks:")
            print(list_tasks(tasks))
            
        elif choice == '3':
            task_id = int(input("Enter task ID to mark complete: "))
            if mark_complete(tasks, task_id):
                print("Task marked complete!")
            else:
                print("Task not found!")
                
        elif choice == '4':
            save_to_csv(tasks)
            print("Tasks saved. Goodbye!")
            break

if __name__ == "__main__":
    main()