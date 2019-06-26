from django.shortcuts import render
from django.http import HttpResponse
from .forms import PrototypeForm, LevelForm
from .models import Prototype, Material_proto, Material_support, Result, Printer
from . import calculs

def home(request):
	return render(request,'outils/home.html',locals())


def level(request):
	level_form = LevelForm(request.POST or None, request.FILES)
	if level_form.is_valid():
		level_form.save()
		level = calculs.calcul_level()
		if level>15:
			return master(request) 
		else :
			return beginner(request)
	return render(request,'outils/level.html',locals())


def beginner(request):
    form_beg = PrototypeForm(request.POST or None, request.FILES)
    if form_beg.is_valid():
        form_beg.save()
        return results(request)
    return render(request,'outils/beginner.html',locals())

def master(request):
    form_mas = PrototypeForm(request.POST or None, request.FILES)
    if form_mas.is_valid():
        form_mas.save()
        return results(request)
    return render(request,'outils/master.html',locals())
    
def results(request):
	calculs.main_calculs()
	result = Result.objects.order_by('-date')[0]
	prototype = Prototype.objects.order_by('-date')[0]
	prin_cost = Printer.objects.get(title = result.printer_cost)
	prin_mate = Printer.objects.get(title = result.printer_mate)
	usage = str(prototype.use)
	return render(request,'outils/results.html',locals())

