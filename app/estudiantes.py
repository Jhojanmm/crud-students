# Definición de la clase Student y del CRUD
class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class StudentDAO:
    def __init__(self, connection):
        self.connection = connection

    def create_student(self, name, age):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO student14 (name, age) VALUES ('{name}', {age})")
        self.connection.commit()
        cursor.execute(f"SELECT * FROM student14 WHERE name='{name}' AND age={age}")
        row = cursor.fetchone()
        return Student(row[0], row[1], row[2])

    def get_all_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM student14")
        rows = cursor.fetchall()
        students = []
        for row in rows:
            students.append(Student(row[0], row[1], row[2]))
        return students

    def get_student(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM student14 WHERE id={id}")
        row = cursor.fetchone()
        return Student(row[0], row[1], row[2]) if row is not None else None

    def update_student(self, id, name, age):
        cursor = self.connection.cursor()
        cursor.execute(f"UPDATE student14 SET name='{name}', age={age} WHERE id={id}")
        self.connection.commit()
        cursor.execute(f"SELECT * FROM student14 WHERE id={id}")
        row = cursor.fetchone()
        return Student(row[0], row[1], row[2])

    def delete_student(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM student14 WHERE id={id}")
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            cursor.execute(f"DELETE FROM student14 WHERE id={id}")
            self.connection.commit()
            return Student(row[0], row[1], row[2])