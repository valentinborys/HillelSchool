from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "postgresql+psycopg2://postgres:Gladiatorr05061518@127.0.0.1:5432/test"
Base = declarative_base()


class Student(Base):
    __tablename__ = 'Students'
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    enrollments = relationship('Enrollment', back_populates='student')


class Course(Base):
    __tablename__ = 'Courses'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100))
    enrollments = relationship('Enrollment', back_populates='course')


class Enrollment(Base):
    __tablename__ = 'Enrollments'
    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Students.student_id'))
    course_id = Column(Integer, ForeignKey('Courses.course_id'))
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def add_course(course_id, course_name):
    session = Session()
    try:
        new_course = Course(course_id=course_id, course_name=course_name)
        session.add(new_course)
        session.commit()
        print(f"Курс {course_name} успішно додано з ID {course_id}.")
        print("")
    except Exception as e:
        session.rollback()
        print(f"Виникла помилка при додаванні курсу: {e}")
    finally:
        session.close()


def add_student_and_enroll(student_id, first_name, last_name, email, course_id):
    session = Session()

    try:
        course = session.query(Course).filter_by(course_id=course_id).first()
        if not course:
            print(f"Курс з ID {course_id} не знайдено.")
            return

        new_student = Student(student_id=student_id, first_name=first_name, last_name=last_name, email=email)
        session.add(new_student)
        session.commit()

        enrollment = Enrollment(student_id=student_id, course_id=course_id)
        session.add(enrollment)
        session.commit()
        print(f"Студента {first_name} {last_name} успішно додано та зареєстровано на курс з ID {course_id}.")
        print("")

    except Exception as e:
        session.rollback()
        print(f"Виникла помилка: {e}")
    finally:
        session.close()

# add_course(1, 'Python Programming')
# add_course(2, 'Data Science')
# add_course(3, 'Web Development')
# add_course(4, 'Database Systems')
# add_course(5, 'Machine Learning')

id = int(input("Введіть id студента: "))
name = str(input("Введіть ім'я студента: "))
surname = str(input("Введіть прізвизще студента: "))
email = str(input("Введіть пошту студента: "))

print("")
print("   Доступні курси:")
courses = ["1: Python Programming", "2: Data Science", "3: Web Development", "4: Database Systems", "5: Machine Learning"]
for x in courses:
    print(x)

print("")
course = int(input("Тепер обери код курсу з вищенаведених данних: "))
print("")

add_student_and_enroll(id, name, surname, email, course)

def get_students_by_course(course_id):
    session = Session()
    try:
        students = session.query(Student).join(Enrollment).filter(Enrollment.course_id == course_id).all()
        if students:
            print(f"Студенти, зареєстровані на курс з ID {course_id}:")
            # for student in students:
            #     print(f"ID: {student.student_id}, Ім'я: {student.first_name}, Прізвище: {student.last_name}, Email: {student.email}")
        else:
            print(f"На курс з ID {course_id} не зареєстровано жодного студента.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    finally:
        session.close()

Session = sessionmaker(bind=engine)
session = Session()

course_id = int(input("Для перегляду всіх студентів введіть ID курсу: "))
print("")

get_students_by_course(course_id)


students_on_course = session.query(Student).join(Enrollment).filter(Enrollment.course_id == course_id).all()

for student in students_on_course:
    print(f"Студент: {student.first_name} {student.last_name}, Email: {student.email}")


print("")
session = Session()

student_id = int(input("Введіть id студента, котрого потрібно видалити: "))

student = session.query(Student).filter_by(student_id=student_id).first()

if student:
    session.delete(student)
    session.commit()
    print("Студента видалено")
    print("")
else:
    print("Студента з таким ID не знайдено.")
    print("")



student_id = int(input("Введіть id студента, котрого потрібно оновити: "))

student = session.query(Student).filter_by(student_id=student_id).first()

if student:
    student.first_name = str(input("Введіть нове ім'я студента: "))
    student.last_name = str(input("Введіть нове прівзище студента: "))
    student.email = str(input('Введіть нову пошту студента: '))
    session.commit()
    print("")
    print("Вітаю! Дані студента успішно оновлені")
else:
    print("Студента з таким ID не знайдено")
    print("")



