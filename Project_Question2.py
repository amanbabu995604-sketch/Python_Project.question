# ### Project_2: Student marks manager
# #stage 1:Averages
# students = {"Aman":[85, 90, 78], "Riya":[92, 88, 95], "Zoya":[70, 65, 80]}
# for name, marks in students.items():
#     average = round(sum(marks)/3, 2)
#     print(name, average)

# #Stage 2: Grades
# students = {"Aman":[85, 90, 78], "Riya":[92, 88, 95], "Zoya":[70, 65, 80]}

# for name, marks in students.items():
#     average = round(sum(marks)/3, 2)
#     if average >= 85:
#         grade = "A"
#     elif average >= 70:
#         grade = "B"
#     elif average >= 50:
#         grade = "c"
#     else:
#         grade = "F"
#     print(name, average, grade)

# #Stage 3: Topper
# students = {"Aman":[85, 90, 78], "Riya":[92, 88, 95], "Zoya":[70, 65, 80]}
# topper = ""
# highest_avg = -1

# for name, marks in students.items():
#     avg = round(sum(marks)/3, 2)

#     if avg > highest_avg:
#         highest_avg = avg
#         topper = name, highest_avg

# print(f"Topper: {topper}")

# #Stage 4: Menu
# students = {"Aman":[85, 90, 78], "Riya":[92, 88, 95], "Zoya":[70, 65, 80]}

# while True:
#     print("\n1. Add Student")
#     print("2. View all")
#     print("3. Show topper")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         name = input("Enter student name: ")

#         marks = []
#         for i in range(3):
#             mark = int(input("Enter marks: "))
#             marks.append(mark)

#         students[name] = marks
#         print("Student added successfully.")

#     elif choice == "2":
#         for name, marks in students.items():
#             avg = round(sum(marks)/len(students), 2)
            
#             if avg >= 85:
#                 grade = "A"
#             elif avg >= 70:
#                 grade = "B"
#             elif avg >= 50:
#                 grade = "C"
#             else:
#                 grade = "F"
#             print(name, avg, grade)

#     elif choice == "3":
#         topper = ""
#         highest_avg = -1

#         for name, marks in students.items():
#             avg = round(sum(marks)/len(students), 2)
#             if avg > highest_avg:
#                 highest_avg = avg
#                 topper = name

#         print(f"Topper: {topper}")

#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Try again.")
        
#Stage 5: Validation

students = {"Aman":[85, 90, 78], "Riya":[92, 88, 95], "Zoya":[70, 65, 80]}

while True:
    print("\n1. Add Student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print("Student already exists!")
        else:
            marks = []

            for i in range(3):
             while True:
                mark = int(input("Enter marks: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid marks! Enter between 0 and 100.")

            students[name] = marks
            print("Student added successfully.")

    elif choice == "2":
        for name, marks in students.items():
            avg = round(sum(marks)/len(students), 2)
            
            if avg >= 85:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "F"
            print(name, avg, grade)

    elif choice == "3":
        topper = ""
        highest_avg = -1

        for name, marks in students.items():
            avg = round(sum(marks)/len(students), 2)
            if avg > highest_avg:
                highest_avg = avg
                topper = name

        print(f"Topper: {topper}")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
        

