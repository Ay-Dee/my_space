from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Heelloo Woorld")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request, a, b):
    return HttpResponse(a+b)

def intro(request, name, age):
    mydict = {
        "name" : name,
        "age" : age,
    }
    return JsonResponse(mydict)

def myfirstpage(request):
    return render(request, 'index.html')

def mysecondpage(request):
    return render(request, 'second.html')

def mythirdpage(request):
    var = "hello world"
    greeting = "hey, how are you?"
    fruits = ['apple', 'mango', 'banana']
    num1, num2 = 10, 7
    ans = num1 > num2
    #print(ans)
    mydict = {
        "var" : var,
        "msg" : greeting,
        "myfruits" : fruits,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans
    }
    return render(request, 'third.html', context=mydict)

def myimagepage(request):
    return render(request, 'imagepage.html')

def myimagepage2(request):
    return render(request, 'imagepage2.html')
def gpa(request):
    
    return render(request,"gpa.html")