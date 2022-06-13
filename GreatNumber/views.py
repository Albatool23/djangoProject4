from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def index(request):

    if request.method == "POST":
        rannum = random.randint(1, 100)
        request.session['num'] = rannum
        print(rannum)
        userinput = int(request.POST["innum"])
        if userinput < rannum:
            return HttpResponseRedirect("/low/")
        elif userinput > rannum:
            return HttpResponseRedirect("/high/")
        elif userinput == rannum:
            return HttpResponseRedirect("/right/")

    return render(request, "index.html")

def low(request):

    if request.method == "POST":
        rannum=request.session['num']
        userinput = int(request.POST["innum"])
        if userinput < rannum:
            return redirect("/low/")
        elif userinput == rannum:
            return redirect("/right/")
        elif userinput > rannum:
            return redirect("/high/")

    return render(request, "low.html")


def high(request):

    if request.method == "POST":
        rannum = request.session['num']
        userinput = int(request.POST["innum"])
        if userinput < rannum:
            return redirect("/low/")
        elif userinput == rannum:
            return redirect("/right/")
        elif userinput > rannum:
            return redirect("/high/")

    return render(request, "high.html")



def right(request):

    return render(request,"right.html")





def Again(request):


  return render(request,'index.html')
# def ret (request):






