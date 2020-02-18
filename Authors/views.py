from django.http import HttpResponse # HttpResponse is used to pass the information back to view 

#Defining a function which will receive request and perform task depending upon function definition 
def index(request):
    return HttpResponse("Welcome to Authors Page")