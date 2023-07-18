from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation
from urllib import request


def index(request):

    return render(request, "django.html" )


def removepunctuations(request):
    inputtext = request.POST.get("text", "default")
    removepunctuations = request.POST.get("removepunctuations", "off")
    capitalize = request.POST.get("capitalize", "off")
    lowercase = request.POST.get("lowercase", "off")
    spaceremover = request.POST.get("spaceremover", "off")
    punctuations = '''"!@~#$%^&*()_+=~{}[]/.,:`;"'''
    name = " "
    if removepunctuations == "on": 
        analyzed = " "
        for char in inputtext:
            if char not in punctuations:
                analyzed = analyzed + char
        inputtext = analyzed 
    if capitalize == "on": 
        analyzed = " "
        for char in inputtext:
            analyzed = analyzed + char.upper()
        inputtext = analyzed  
    if lowercase == "on": 
        analyzed = " "
        for char in inputtext:
            analyzed = analyzed + char.lower()
        inputtext = analyzed         
    if spaceremover == "on":
        analyzed = " "
        for index,char in enumerate(inputtext):
            if not (inputtext[index] == " " and inputtext[index + 1] == " "):
                analyzed = analyzed + char
        inputtext = analyzed        
    if removepunctuations != "on" and capitalize != "on" and lowercase != "on" and spaceremover != "on":
        return HttpResponse("<h3 style = 'color: red;'>can't work if you don't select anything!<h3>")
        
    #else:
        #return HttpResponse("<h1 style = 'color: red;'>can't work if you don't select anything!<h1>")
    
    input_text = {'text': "your text has been completely formatted based on your request(s) ", 'output': analyzed}
   
                  
            
    return render(request, "result.html", input_text )

##def 
   
   ## else:
    #    return HttpResponse("<h1 style = 'color: red;'>can't work if you don't select anything!<h1>")                 
            
   # return render(request, "result.html", input_text )
    

            
        
        