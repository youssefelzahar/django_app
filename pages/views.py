from django.shortcuts import render
from django.http import HttpResponse
from .models import login
from .forms import LoginForm

# Create your views here.
def index(request):
   
  if request.method=='POST':   
    data_form=LoginForm(request.POST)

    if data_form.is_valid():
     data_form.save()

    #username=request.POST.get('user_name')
    #userpassword=request.POST.get('user_pasword')
    #data=login(user_name=username,user_pasword=userpassword)
    #data.save()

 


    return render(request,'index.html',{'lf':LoginForm})