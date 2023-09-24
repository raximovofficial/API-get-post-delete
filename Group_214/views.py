from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from django.views.generic import ListView
from .forms import StudentForms

# Create your views here.
# class StudentListView(ListView):
#     def get(self, request):
#         students = Student.objects.all()
#         name = Student.objects.all()
#         return render(request, 'student_list.html', {'add': students, 'name': name})
#
# class StudentFormCreateView(CreateView):
#     model = Student
#     form_class = StudentForms
#     template_name = 'student_form.html'  # Create a template for the form
#     success_url = reverse_lazy('student_list')  # Redirect after successful form submission
#
class StudentsView(APIView):
    def get(self,request):
        students = Student.objects.all().values()
        return Response({'student': list(students)})

    def post(self, request):
        new_student = Student.objects.create(
            name=request.data['name']
        )
        return Response({'new_student': model_to_dict(new_student)})

    def delete(self, request):
        try:
            student_id = request.data['student_id']
            Student.objects.filter(pk= student_id).delete()
            return Response({'result': 'success','desc': f'Student with id{student_id} successfully deleted'})
        except:
            return Response({'result': 'failed', 'desc': '403'})
