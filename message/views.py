from django.shortcuts import render

# Create your views here.


def getform(request):
    return render(request=request, template_name='message_from.html')