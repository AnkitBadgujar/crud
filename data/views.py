from django.shortcuts import redirect, render
from django.http import request
from django.views import View
from .models import Student
from .forms import AddStudentForm

# Create your views here.

class Home(View):
    def get(self,request):
        student_data = Student.objects.all()
        return render(request,'home.html', {'studata' : student_data})


class AddStudent(View):
    def get(self,request):
        fm = AddStudentForm()
        return render(request,'add.html', {'form':fm})

    def post(self,request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'add.html', {'form':fm})

class DeleteStudent(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')

class EditStudent(View):
    def get(self,request,id):
        stud = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stud)
        return render(request,'edit.html', {'form':fm})

    def post(self,request,id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return redirect('/')