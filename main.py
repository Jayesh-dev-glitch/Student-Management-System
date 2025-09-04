import mysql.connector
#connect to mysql
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayesh@#4847",
    database="student_db"
)
cursor=conn.cursor()

#create students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
            student_id int auto_increment primary key,
            name varchar(100),
            gender varchar(10),
            python_marks int,
            sql_marks int,
            percentage float
            )
    """)

# Create Student
def create_student(name,gender,python_marks,sql_marks):
    total_obtained=python_marks+sql_marks
    percentage=(total_obtained/200)*100
    sql="""
       insert into students (name,gender,python_marks,sql_marks,percentage)
       values(%s,%s,%s,%s,%s)
    """
    values=(name,gender,python_marks,sql_marks,percentage)
    cursor.execute(sql,values)
    conn.commit()
    print("Student record added successfully")

# Display all students
def read_student():
    cursor.execute("Select * from students")
    for student in cursor.fetchall():
        print(student)

# Update student marks
def update_student(student_id,python_marks,sql_marks,percentage):
    sql="""
       update students
       set python_marks=%s,sql_marks=%s,percentage=%s
       where student_id=%s
    """
    values=(python_marks,sql_marks,percentage,student_id)
    cursor.execute(sql,values)
    conn.commit()
    print("Student record updated.")

# Delete student
def delete_student(student_id):
    sql="Delete from students where student_id=%s"
    cursor.execute(sql,(student_id,))
    conn.commit()
    print("Student record deleted.")

#Main Program
if __name__=="__main__":
    while True:
        print("\n--- Student Management System ---")
        print("1.Add Student")
        print("2.View Students")
        print("3.Update Student Marks")
        print("4.Delete Student")
        print("5.Exit")

        choice=input("Enter your choice: ")
        if choice=='1':
            name=input("Enter student name: ")
            gender=input("Enter gender(Male/Female): ")
            python_marks=int(input("Enter Python marks (out of 100): "))
            sql_marks=int(input("Enter SQL marks(out of 100): "))
            create_student(name,gender,python_marks,sql_marks)

        elif choice=='2':
            read_student()
        
        elif choice=='3':
            student_id=input("Enter student id to update: ")
            python_marks=int(input("Enter new Python marks (out of 100): "))
            sql_marks=int(input("Enter new SQL marks(out of 100): "))
            total_obtained=python_marks+sql_marks
            percentage= percentage=(total_obtained/200)*100
            update_student(student_id,python_marks,sql_marks,percentage)

        elif choice=='4':
            student_id=int(input("Enter student id to delete: "))
            delete_student(student_id)
        
        elif choice=='5':
            print("Exiting program.")
            break
        else:
            print("Invlid choice.Try again.")
    
# Close connection & cursor
cursor.close()
conn.close()