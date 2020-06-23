from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BookForm
from .models import Book
from django.contrib import messages
# Create your views here.

def home_view(request):
	# return HttpResponse("Hello World") 			   #requires "from django.http import HttpResponse"
	
	# return HttpResponse("<h1> Hello world </h1>")     #requires "from django.http import HttpResponse"
	return render(request, "home.html", {})


def create_view(request):
	form=BookForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		messages.info(request, "Book details saved!")
		form.save()
		form=BookForm()

	context={
		'context_form': form	
	}
	return render(request, 'create.html', context)


def edit_view(request):
	obj=Book.objects.get(id=24)
	form=BookForm(request.POST or None, request.FILES or None, instance=obj)
	if form.is_valid():
		form.save()
		form=BookForm()
	context={
	'context_form': form
	}
	return render(request, 'edit.html', context)


def view_view(request):
	obj=Book.objects.get(id=1)
	context={
	'context_obj': obj
	}
	return render(request, 'view.html', context)

def delete_view(request):
	obj=Book.objects.get(id=35)
	if request.method=='POST':
		obj.delete()
		return redirect("/")
	context={
	'context_obj': obj
	}
	return render(request, 'delete.html', context)

#############

def edit_global_view(request, id):
	obj=Book.objects.get(id=id)
	form=BookForm(request.POST or None, request.FILES or None, instance=obj)
	if form.is_valid():
		form.save()
		messages.info(request, "Book details changed!")
		form=BookForm()
	context={
	'context_form': form
	}
	return render(request, 'edit.html', context)


def view_global_view(request, id):
	obj=Book.objects.get(id=id)
	context={
	'context_obj': obj
	}
	return render(request, 'view.html', context)

def delete_global_view(request, id):
	# obj=Book.objects.get(id=id)
	obj=get_object_or_404(Book, id=id)

	if request.method=='POST':
		obj.delete()
		return redirect("/delete_list")
	context={
	'context_obj': obj
	}
	return render(request, 'delete.html', context)

##############


def edit_list_view(request):
	queryset=Book.objects.all()
	context={
	'context_qs': queryset
	}
	return render(request, 'edit_list_view.html', context)


def view_list_view(request):
	queryset=Book.objects.all()
	context={
	'context_qs': queryset
	}
	return render(request, 'view_list_view.html', context)

def delete_list_view(request):
	queryset=Book.objects.all()
	context={
	'context_qs': queryset
	}
	return render(request, "delete_list_view.html", context)