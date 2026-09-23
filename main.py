from student_function import Student
from database import mydb, cursor

s = Student()



while True:
    print("\n-----Student Manegment System-----\n")
    try:
        choose = int(input("(1)Add Student\n"
                           "(2)View All Students\n"
                           "(3)Search Student\n"
                           "(4)Update Student\n"
                           "(5)Delete Student\n"
                           "(6)Search By Name\n"
                           "(7)Highest Mark\n"
                           "(8)Lowest Mark\n"
                           "(9)Total Student\n"
                           "(10)Average Mark\n"
                           "(11)Exit\n"))
    except ValueError:
        print("!!!!!Enter The Valid Option!!!!!")

    # Add Student
    if choose == 1:
        s.create_id()
    # View Student
    elif choose == 2:
        s.view_students()

    # Search Student
    elif choose == 3:
        s.search_student()

    # Update Student
    elif choose == 4:
        s.update_student()

    # Delete Student
    elif choose == 5:
        s.delete_student()

    elif choose == 6:
        s.search_by_name()

    elif choose == 7:
        s.highest_mark()

    elif choose == 8:
        s.lowest_mark()

    elif choose == 9:
        s.average_mark()

    elif choose == 10:
        s.total_student()
    # Exit
    elif choose == 11:
        print("-----THANKS FOR USING IT-----\n")
        break

    else:
        print("\n!!!!!--Please Choose right Option--!!!!!\n")

cursor.close()
mydb.close()