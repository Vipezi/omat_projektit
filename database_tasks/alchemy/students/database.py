#! /usr/bin/python3

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
# Establish connection to in-memory database.
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)

# Import declarative_base that is required to create the ORM tables
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    studentId = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False) # I tried this as a float first, but it crashed as predicted.
    courses = relationship("Course", secondary="studentcourse", back_populates="students") #, cascade = "all, delete-orphan", single_parent = True) I tried if the error was due to this, but the lastname type was wrong
    
class Course(Base):
    __tablename__ = "courses"
    courseId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    students = relationship("Student", secondary = "studentcourse", back_populates="courses") #, cascade = "all, delete-orphan", single_parent = True)
    
class StudentCourse(Base):
    __tablename__ = "studentcourse"
    studentId = Column(Integer, ForeignKey("students.studentId"), primary_key=True)
    courseId = Column(Integer, ForeignKey("courses.courseId"), primary_key=True)


# Finally, remember to create the tables with this
Base.metadata.create_all(engine)

# Create session to interact with the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()