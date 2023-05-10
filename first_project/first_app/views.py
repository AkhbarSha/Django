from django.shortcuts import render
from first_app.models import Program, Student

# Create your views here.
from django.http import HttpResponse
# 'request' name is convention. It can be some other name too.
def index(request) :
   program_values = Program.objects.all()
   fruits = ['apple', 'banana', 'kiwi', 'guava', 'mango']
   my_dict = { 'fruit_list': fruits , 'program_rows' : program_values,}
   return render(request, 'index.html', my_dict)



def process_form(request) :
    username = request.GET.get('user')
    password = request.GET.get('pwd')
    print(username, password)
    return render(request, 'form.html')

from django.http import HttpResponseRedirect
from django.shortcuts import render
 
from .forms import StudentForm          
 
def get_student(request):  
  print("HI")  
  if request.method == 'POST':          
    form = StudentForm(request.POST)  
    print("sd")   
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
        s_year=form.cleaned_data['year']
        print(s_name)
 
    return HttpResponseRedirect('/student/')
  else: 
    form =StudentForm()
    return render(request, 'StudentForm.html', {'form': form})