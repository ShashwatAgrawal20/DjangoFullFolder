# aapne ko iss ke andar ek aurgument bhi dena hota hai reuqests ye nhi diya to ek error milta hai 

from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    # aapan iss ko kuch iss tarah se bhi iterate kr skte hai bhot kam ka hai ye 
    a = {'Name':'Shashwat'}
    return render(request, 'index.html', a)
# aapan iss ke jagah ek tempelate bhi laga skte hai .. vo jada aasan hota hai..

# Aapan  iss me vo bhi dal skte hai html ka .. 
# def about(request):
#     return HttpResponse("About Shashwat Agrawal")

def analyze(request): 
    # Get the text 
    djtext = (request.POST.get('text', 'default'))
    print(djtext)

    # Agr aapan ne checkbox pr tick kra hai to ye on aayegi aur nhi kra hai to ye of aayengi
    removepunc = (request.POST.get('removepunc', 'off'))

    Capatilize = (request.POST.get('Capatilize', 'off'))

    Lower =(request.POST.get('Lower', 'off'))

    newlineremover = (request.POST.get('newlineremover', 'off'))

    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))

    charcount = (request.POST.get('charcount', 'off'))

    # print(removepunc)
    #Analyse the text
    # analyzed = djtext
    if removepunc == "on":
        punctutations = '''!()-[]{}:;'",<>./?@#$%^&*_`~'''
    
        analyzed = ""
        for char in djtext:
            if char not in punctutations:
                analyzed = analyzed+char
        params = {"purpose":"Removepunctuation", "analyzed_text":analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (Capatilize =="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {"purpose":"Changed to Upper case", "analyzed_text":analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (Lower =="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.lower()
        params = {"purpose":"Changed to Lower case", "analyzed_text":analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if (newlineremover =="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed+char
        params = {"purpose":"new line has been removed", "analyzed_text":analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if (extraspaceremover =="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed+char
        params = {"purpose":"new line has been removed", "analyzed_text":analyzed}
        djtext = analyzed
    
# This helps in the Charactere Counting
    if (charcount=="on"):
        analyzed=""
        analyzed = analyzed, len(djtext)
        # analyzed = analyzed, lambda djtext:len(djtext)
        # analyzed()
        params = {"purpose":"counts the character", "analyzed_text":analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
            

    
    return render(request, 'analyze.html', params)


# def capfirst(request):
#     return HttpResponse("Capatilize the first letter")

# def count(request):
#     return HttpResponse("Count the number of alphabets")


# def newline(request):
#     return HttpResponse("newline")


# sha = input("enter the text")
# print(len(sha))