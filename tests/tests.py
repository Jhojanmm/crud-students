import unittest
from unittest.mock import MagicMock
from app.estudiantes import Student, StudentDAO

class TestStudentDAO(unittest.TestCase):
    def setUp(self):
        self.dao = MagicMock(spec=StudentDAO)

    def test_create_student(self):
        student = Student(self, "John Doe", 20)
        self.dao.create_student.return_value = student
        result = self.dao.create_student("John Doe", 20)
        self.assertEqual(result, student)

    def test_get_all_students(self):
        students = [Student(self, "John Doe", 20), Student(self, "Jane Doe", 21)]
        self.dao.get_all_students.return_value = students
        result = self.dao.get_all_students()
        self.assertEqual(result, students)

    def test_get_student(self):
        student = Student(self, "John Doe", 20)
        self.dao.get_student.return_value = student
        result = self.dao.get_student(1)
        self.assertEqual(result, student)

    def test_update_student(self):
        student = Student(self, "Jane Doe", 21)
        self.dao.update_student.return_value = student
        result = self.dao.update_student(1, "Jane Doe", 21)
        self.assertEqual(result, student)

    def test_delete_student(self):
        student = Student(self, "John Doe", 20)
        self.dao.delete_student.return_value = student
        result = self.dao.delete_student(1)
        self.assertEqual(result, student)

if __name__ == '__main__':
    unittest.main()