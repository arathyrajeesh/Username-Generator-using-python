#Create a To-Do List App where users can add, view, mark done, and delete tasks.
tasks = []
def show_task():
    print("\nYour Task")
    if not tasks:
        print('there is no task')
    else:
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")
def add_task():
    task=input('Enter Task :')
    tasks.append(task)
    
def delete_task():
    show_task()
    num=int(input('Task number to be Delete :')) -1
    if 0 <= num < len(tasks):
        tasks.pop(num)
def mark_done():
    show_task()
    num=int(input('Task number to be Mark : ')) - 1
    if 0 <=num < len(tasks):
        tasks[num] += '**'
def menu():
    while True:
        print('\n1.Add Task')
        print('2.Delete Task')
        print('3.View Task')
        print('4.Mark Task')
        print('5.Exit')
        
        choice = input('Enter Choice :')
        
        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            show_task()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            break
        else:
            print('Invalid choice')
menu()
