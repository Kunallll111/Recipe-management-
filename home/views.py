from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    peoples = [{'name': 'Kunal rajput',  'age': 23},
               {'name': 'Abhay Pratap',  'age': 15},
               {'name': 'vatsal Jain',  'age': 19},
               {'name': 'Anshul Kumar',  'age': 13},
               {'name': 'Abhishek kaala',  'age': 27},
               {'name': 'Aashu Scam',  'age': 12}]
    return render(request, "index.html", context={'peoples': peoples})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def success_page(request):
    print("*" * 10)
    return HttpResponse("""<h1>This is a succces page<h1>
    <P ALIGN=LEFT>This is aligned left. This is the default.</P>
<P ALIGN=CENTER>This is aligned center.</P>
<P ALIGN=RIGHT>This is aligned right.</P>""")
