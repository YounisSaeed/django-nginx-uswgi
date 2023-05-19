from django.shortcuts import render

# Create your views here.
def home(request):
    contex = {
        'sent':'WELCOME TO LOADBALANCE SERVER 2'
    }
    return render(request,'app/index.html',contex)