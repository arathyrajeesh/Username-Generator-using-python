# Make a Student Gradebook to enter marks for students and display averages, highest, and lowest marks.

grade_book = []

def add_mark():
    s_name = input("Enter the student name: ")
    s_mark = float(input("Enter mark: "))   
    data = {
        "Name": s_name,
        "Mark": s_mark
    }
    grade_book.append(data)
    print("Mark added!")

def view_student():
    print("\nStudents:")
    if not grade_book:
        print("No students yet!")
    else:
        for i, student in enumerate(grade_book, start=1):
            print(f"{i}. {student['Name']} - {student['Mark']}")

def display_average():
    if not grade_book:
        print("No marks entered yet!")
        return
    marks = [student["Mark"] for student in grade_book]
    avg = sum(marks) / len(marks)
    print(f"Average mark: {avg:.2f}")

def highest_mark():
    if not grade_book:
        print("No marks entered yet!")
        return
    top = grade_book[0]
    for student in grade_book:
        if student["Mark"] > top["Mark"]:
            top = student
    print(f"Highest mark: {top['Name']} - {top['Mark']}")

def lowest_mark():
    if not grade_book:
        print("No marks entered yet!")
        return
    low = grade_book[0]
    for student in grade_book:
        if student["Mark"] < low["Mark"]:
            low = student
    print(f"Lowest mark: {low['Name']} - {low['Mark']}")

def student():
    while True:
        print("\nGrade Book")
        print("1. Add Mark")
        print("2. View Students")
        print("3. Display Average")
        print("4. Highest Mark")
        print("5. Lowest Mark") 
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))        
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            add_mark()
        elif choice == 2:
            view_student()
        elif choice == 3:
            display_average()
        elif choice == 4:
            highest_mark()        
        elif choice == 5:
            lowest_mark()
        elif choice == 6:
            print("Exiting Grade Book. All Done!")
            break
        else:
            print("Invalid choice! Try again.")

student()
