from django.shortcuts import render
app_name='anything'
# Create your views here.
def condition(request):
    d={'name':'ravi','age':23}
    return render(request,'condition.html' ,context=d)

def ifelse_condition(request):
    d={'name':'ravi','age':13}
    return render(request,'ifelse_condition.html' ,context=d)

def ifelif_condition(request):
    d={'name':'ravi','age':23}
    return render(request,'ifelif_condition.html' ,context=d)

def nestedif_condition(request):
    d={'name':'ravi','age':23}
    return render(request,'nestedif_condition.html' ,context=d)

