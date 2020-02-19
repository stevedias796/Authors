from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse, JsonResponse # HttpResponse is used to pass the information back to view 
from .models import *
#Defining a function which will receive request and perform task depending upon function definition 
def index(request):
    response = ""
    a = Author.objects.all()
    authors_list = []
    books_list = []
    for x in a:
        authors_list.append(x.author_name)
        response += x.author_name+"<ul>"
        print(x.id)
        b = Author.objects.get(pk=x.id)
        books = b.book_set.all()
        for y in books:
            books_list.append(y.book_names)
            response += "<li>"+y.book_names+"</li>"
        response += "</ul>"
    return HttpResponse(response)

def home(request):
    names = Author.objects.all()
    resp = []
    for x in names:
        print(x)
        resp.append(x)
    return render(request, "home.html", {'authors':resp})


def new_home(request):
    names = Author.objects.all()
    resp = []
    for x in names:
        print(x)
        resp.append(x)
    return render(request, "home_new.html", {'authors':resp})

def searching(request):
    print("in searching")
    auth_name = request.POST.get('auth_name')
    response=""
    name = Author.objects.filter(author_name__iexact=auth_name).values_list('id')
    if len(name) == 0:
        res = {"text":"No books found, Kindly check whether the author's name is correct", 'status':-1}
        return JsonResponse(res)
    books = Book.objects.filter(author=name[0])
    if len(books) == 0:
        mess = "Sorry currently we have no books written by "+auth_name
        res = {"text":mess, 'status':-1}
        return JsonResponse(res)
    for x in books:
        if len(response) == 0:
            response += str(x)
        else:
            response += "|"+str(x)
    #print(response)
    res = {"text":response, 'status': 0}
    return JsonResponse(res)
