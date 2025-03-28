from django.shortcuts import render

# Create your views here.
def registration_list(request):
    return render(request, 'student_registration/registration_list.html')