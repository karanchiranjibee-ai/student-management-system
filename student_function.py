from database import mydb, cursor


class Student:

    def verify_admin(self):
        id_ = int(input("Enter ID"))
        password = input("Enter Password")

        cursor.execute(
            "SELECT * FROM passs WHERE id = %s AND pass = %s",
            (id_, password)
        )

        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    def create_id(self):
        id = input("Enter the id")
        name = input("Enter the name")
        Age = input("Enter the Age")
        Mark = int(input("Enter the Marks"))
        if Mark > 100 or Mark < 0:
            print("Enter th valid mark")
            return
        if Mark >= 90:
            grade = "O"
        elif Mark >= 80:
            grade = "E"
        elif Mark >= 70:
            grade = "A"
        elif Mark >= 60:
            grade = "B"
        elif Mark >= 50:
            grade = "C"
        elif Mark >= 40:
            grade = "D"
        else:
            grade = "F"

        cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s)", (id, name, Age, Mark, grade))

        mydb.commit()
        print("Create Student id Successfully")

    def view_students(self):

        if self.verify_admin():

            cursor.execute("""SELECT * FROM student""")
            print("ID | NAME | AGE | MARK | GRADE")
            print("--------------------------------")

            for i in cursor:
                print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "|")
        else:
            print("You Enter Wrong ID or PASSWORD")

    def search_student(self):
        if self.verify_admin():

            id = int(input("Enter The id "))
            cursor.execute("SELECT * FROM student WHERE id = %s", (id,))

            result = cursor.fetchall()

            if result:
                print("id | name | age | mark | grade")
                for i in result:
                    print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4])
            else:
                print("Account Not Found")
        else:
            print("You Enter Wrong ID or PASSWORD")

    def update_student(self):

        if self.verify_admin():
            try:
                id = int(input("Enter the id"))
            except ValueError:
                print("Please enter the Valid ID")
                return
            cursor.execute("SELECT * FROM student WHERE id = %s", (id,))

            result = cursor.fetchone()

            if result:
                try:
                    change = int(input("1. Name Update\n"
                                       "2. Age Update\n"
                                       "3. Mark Update\n"
                                       "4. Grade Update\n"))
                except ValueError:
                    print("Enter Valid Option")
                    return

                # Name Change
                if change == 1:
                    name = input("Enter the Name To change")
                    cursor.execute("""UPDATE student
                                         SET name = %s WHERE id = %s""", (name, id))
                    mydb.commit()
                    print("\n++++Update Successfully++++\n")

                # Age Change
                elif change == 2:
                    age = input("Enter the age To change")
                    cursor.execute("""UPDATE student
                                         SET age = %s WHERE id = %s""", (age, id))
                    mydb.commit()
                    print("\n++++Update Successfully++++\n")

                # Mark Change
                elif change == 3:
                    mark = input("Enter the Mark To change")
                    cursor.execute("""UPDATE student
                                         SET mark = %s WHERE id = %s""", (mark, id))
                    mydb.commit()
                    print("\n++++Update Successfully++++\n")

                # Grade Change
                elif change == 4:
                    grade = input("Enter the Grade To change")
                    cursor.execute("""UPDATE student
                                         SET grade = %s WHERE id = %s""", (grade, id))
                    mydb.commit()
                    print("\n++++Update Successfully++++\n")

                else:
                    print("You Choose Wrong Option")
            else:
                print("Account Not Found")
        else:
            print("You Enter Wrong ID or PASSWORD")

    def delete_student(self):

        if self.verify_admin():
            try:
                id = int(input("Enter The ID To delete"))

            except ValueError:
                print("Please enter a valid id")
                return

            cursor.execute(
                "SELECT * FROM student WHERE id = %s",
                (id,)
            )

            result = cursor.fetchone()

            if result:
                cursor.execute(
                    "DELETE FROM student WHERE id = %s",
                    (id,)
                )

                mydb.commit()
                print("DELETED SUCCESSFULLY")

            else:
                print("Account Not Found")

        else:
            print("You Enter Wrong ID or PASSWORD")

    def search_by_name(self):
        if self.verify_admin():
            name = input("Enter the name")
            cursor.execute("SELECT * FROM student WHERE name = %s", (name,))
            result = cursor.fetchall()
            if result:
                print("id | name | age | mark | grade")
                for i in result:
                    print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4])
            else:
                print("Account Not Found")
        else:
            print("Enter Valid Password")

    def highest_mark(self):
        if self.verify_admin():
            cursor.execute("""SELECT * FROM student 
                              WHERE mark = (SELECT max(mark) FROM student)""")
            result = cursor.fetchall()
            if result:
                print("\nid | name | age | mark | grade")
                for i in result:
                    print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "\n")
            else:
                print("NO Student Found")
        else:
            print("WRONG PASSWORD")

    def lowest_mark(self):
        if self.verify_admin():
            cursor.execute("SELECT * FROM student WHERE mark = (SELECT min(mark) FROM student)")
            result = cursor.fetchall()
            if result:
                print("\nid | name | age | mark | grade")
                for i in result:
                    print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "\n")
            else:
                print("NO Student FOUND")
        else:
            print("WRONG PASSWORD")

    def average_mark(self):
        if self.verify_admin():
            cursor.execute("SELECT avg(mark) FROM student")
            result = cursor.fetchall()
            print(f"\nThe Average Mark {result[0]}\n")
        else:
            print("WRONG PASSWORD")

    def total_student(self):
        if self.verify_admin():
            cursor.execute("SELECT count(id) FROM student")
            result = cursor.fetchone()
            print("Total No of students :",result[0])
        else:
            print("WRONG PASSWORD")

