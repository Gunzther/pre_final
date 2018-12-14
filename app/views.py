from django.shortcuts import render
from .models import Semester, Course
from django.http import  HttpResponseRedirect
from django.urls import reverse

def index (request):
  template_name = 'app/index.html'
  semester_all = Semester.objects.all()
  context = {'semester_all' : semester_all}
  return render(request, template_name, context)

def CourseView(request,semester_id,term_id):
  template_name = 'app/course.html'
  semester = Semester.objects.get(id=semester_id)
  context = {'semester' : semester}
  return render(request, template_name, context)

def addCourse(request,semester_id,term_id):
  id = request.POST['id']
  title = request.POST['title']
  c = request.POST['credit']
  semester = Semester.objects.get(id=semester_id)
  c1 = semester.course_set.create(course_id=id,course_title=title,grade=g,credit=c)
  c1.save()
  return HttpResponseRedirect(reverse('GPA:course', args=(semester_id,term_id,)))
