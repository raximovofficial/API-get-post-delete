from django.urls import path
# from .views import StudentListView,StudentFormCreateView
from .views import StudentsView

urlpatterns = [
    # path('students/', StudentListView.as_view(), name='student_list'),
    # path('students/add/', StudentFormCreateView.as_view(), name='student_create'),
    path('', StudentsView.as_view())
]