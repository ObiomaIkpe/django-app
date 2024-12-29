# from django.http import HttpResponse

# def homepage(request):
#     return HttpResponse("hello world!")

# def about(request):
#     return HttpResponse("about page")


from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')