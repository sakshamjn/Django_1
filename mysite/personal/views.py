from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If want to contact me, email me at :', 'sakshamjn655@gmial.com', 'It\'s been a pleasure to hear from you']})
