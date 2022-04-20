from django.shortcuts import render
from django.http import JsonResponse
from ajaxapp.models import User
from .forms import StudentRegistration

# Create your views here.
def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'home.html',{'form':form , 'stu': stud})

def save_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            user = User(name = name, email = email, password = password)
            user.save()
            stu= User.objects.values()
            # print(stu)
            stud=list(stu)
            return JsonResponse({'status':'Save', 'stud':stud})
        else:
            return JsonResponse({'status': 0})



def show_data(request):
    if request.method == 'POST':
        stu= User.objects.values()
        stud = list(stu)
        return JsonResponse({'status':'Save', 'stud':stud})


def all_data(request):
    if request.method == 'POST':
        stu = User.objects.values()
        stud = list(stu)

        return JsonResponse({'status':'Save', 'stud':stud})