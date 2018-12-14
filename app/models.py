from django.db import models

# Create your models here.
class Semester(models.Model):
    semester = models.IntegerField()
    def __str__(self):
        return str(self.semester)

class Course(models.Model):
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    course_id = models.IntegerField()
    course_title = models.CharField(max_length=100)
    credit = models.IntegerField(default=1)

    def __str__(self):
        return "Semester " + str(self.semester) + " | " + str(self.course_id) + " | " +  self.course_title

    class Meta():
      ordering = ['semester', 'course_id']
