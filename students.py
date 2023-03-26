import pyodbc
import unittest

# Configuración de la conexión a la base de datos
connection = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=CESARPORTO;'
    'Database = prueba;'
    'Trusted_Connection=yes;'
)

# Definición de la clase Student y del CRUD
class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class StudentDAO:
    def create_student(self, name, age):
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO student14 (name, age) VALUES ('{name}', {age})")
        connection.commit()
        cursor.execute(f"SELECT * FROM student14 WHERE name='{name}' AND age={age}")
        row = cursor.fetchone()
        return Student(row[0], row[1], row[2])

    def get_all_students(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student14")
        rows = cursor.fetchall()
        students = []
        for row in rows:
            students.append(Student(row[0], row[1], row[2]))
        return students

    def get_student(self, id):
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM student14 WHERE id={id}")
        row = cursor.fetchone()
        return Student(row[0], row[1], row[2]) if row is not None else None

    def update_student(self, id, name, age):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE student14 SET name='{name}', age={age} WHERE id={id}")
        connection.commit()
        cursor.execute(f"SELECT * FROM student14 WHERE id={id}")
        row = cursor.fetchone()
        return Student(row[0], row[1], row[2])

    def delete_student(self, id):
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM student14 WHERE id={id}")
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            cursor.execute(f"DELETE FROM student14 WHERE id={id}")
            connection.commit()
            return Student(row[0], row[1], row[2])

# Pruebas unitarias
class TestStudents(unittest.TestCase):

    # Configuración de prueba
    def setUp(self):
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE student14 (id INT IDENTITY(1,1) PRIMARY KEY, name VARCHAR(50), age INT)")
        connection.commit()

    # Eliminar tabla después de cada prueba
    def tearDown(self):
        cursor = connection.cursor()
        cursor.execute("DROP TABLE student14")
        connection.commit()

    # Prueba para crear un estudiante
    def test_create_student(self):
        dao = StudentDAO()
        student = dao.create_student('Juan', 20)
        self.assertIsNotNone(student.id)
        self.assertEqual(student.name, 'Juan')
        self.assertEqual(student.age, 20)
    # Prueba para obtener un estudiante existente
    def test_get_student(self):
        dao = StudentDAO()
        dao.create_student('Juan', 20)
        student = dao.get_student(1)
        self.assertIsNotNone(student)
        self.assertEqual(student.name, 'Juan')
        self.assertEqual(student.age, 20)

    # Prueba para obtener un estudiante que no existe
    def test_get_nonexistent_student(self):
        dao = StudentDAO()
        student = dao.get_student(1)
        self.assertIsNone(student)

    # Prueba para actualizar un estudiante existente
    def test_update_student(self):
        dao = StudentDAO()
        dao.create_student('Juan', 20)
        updated_student = dao.update_student(1, 'Juan Pablo', 22)
        self.assertIsNotNone(updated_student)
        self.assertEqual(updated_student.id, 1)
        self.assertEqual(updated_student.name, 'Juan Pablo')
        self.assertEqual(updated_student.age, 22)


        # Prueba para crear un estudiante sin nombre
    def test_create_student_without_name(self):
        dao = StudentDAO()
        student = dao.create_student('', 20)
        self.assertIsNotNone(student.id)
        self.assertEqual(student.name, '')
        self.assertEqual(student.age, 20)
        
        # Verificar que el estudiante exista en la base de datos
        db_student = dao.get_student(student.id)
        self.assertIsNotNone(db_student)
        self.assertEqual(db_student.name, '')
        self.assertEqual(db_student.age, 20)


        # Prueba para eliminar un estudiante existente
    def test_delete_student(self):
        dao = StudentDAO()
        dao.create_student('Juan', 20)
        student = dao.delete_student(1)
        self.assertIsNotNone(student)
        self.assertEqual(student.name, 'Juan')
        self.assertEqual(student.age, 20)

        # Verificar que el estudiante ya no exista en la base de datos
        db_student = dao.get_student(student.id)
        self.assertIsNone(db_student)

        # Verificar que no se pueda eliminar un estudiante que no existe
        non_existent_student = dao.delete_student(1)
        self.assertIsNone(non_existent_student)
    
        # Prueba para eliminar un estudiante existente
    def test_delete_student(self):
        dao = StudentDAO()
        dao.create_student('Juan', 20)
        deleted_student = dao.delete_student(1)
        self.assertIsNotNone(deleted_student)
        self.assertEqual(deleted_student.id, 1)
        self.assertEqual(deleted_student.name, 'Juan')
        self.assertEqual(deleted_student.age, 20)
        non_existent_student = dao.get_student(1)
        self.assertIsNone(non_existent_student)





if __name__ == '__main__':
    unittest.main()
