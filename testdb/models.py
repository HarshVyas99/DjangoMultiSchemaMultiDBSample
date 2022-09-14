from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    class Meta:
        app_label = 'testdb'
        db_table='django\".\"teacher'
        
class Student(models.Model):
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    class Meta:
        app_label = 'testdb'
        db_table='custom\".\"student'
        
        
class Studenttest(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    class Meta:
        app_label = 'testdb'
        db_table='users\".\"studenttest'
        
class Studentprod(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    class Meta:
        app_label = 'testdb'
        db_table='users\".\"studentprod'
        
class Teachertest(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    class Meta:
        app_label = 'testdb'

class Teacherprod(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    class Meta:
        app_label = 'testdb'