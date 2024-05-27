from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120, null=False)
    last_name = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=120, null=False, unique=True)
    password = models.CharField(max_length=120, null=False)
    connected = models.BooleanField(default=False, null=False)
    status = models.BooleanField(default=False, null=False)
    selected_subject = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'status': self.status,
        }

class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120, null=False)
    last_name = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=120, null=False, unique=True)
    password = models.CharField(max_length=120, null=False)
    connected = models.BooleanField(default=False, null=False)
    status = models.BooleanField(default=False, null=False)
    selected_subject = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'status': self.status,
        }

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=120, null=False, unique=True)

    def __str__(self):
        return self.subject_name

class RoomRequest(models.Model):
    id = models.AutoField(primary_key=True)
    instructor_confirmation = models.BooleanField(null=True, default=None)
    status = models.BooleanField(null=True, default=None)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def to_dict(self):
        return {
            'id': self.id,
            'instructor_confirmation': self.instructor_confirmation,
            'status': self.status,
            'student_id': self.student.id,
            'instructor_id': self.instructor.id,
            'category_id': self.category.id,
        }

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_request = models.OneToOneField(RoomRequest, on_delete=models.CASCADE, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    room_status = models.BooleanField(default=True, null=False)
    student_finished = models.BooleanField(default=False, null=False)
    instructor_finished = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f"Room {self.id}"