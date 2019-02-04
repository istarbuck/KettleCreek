from django.http import HttpResponse, Http404
from KettleCreek.models import Menu
from django.shortcuts import render_to_response
from django.template import RequestContext

def menu(request, cat):
	categories = Menu.objects.filter(category=cat)
	cats = Menu.objects.all()
	variables = RequestContext(request, {
		'cats': cats,
		'category': cat,
		'categories': categories
		})
	return render_to_response('menu.html', variables)
