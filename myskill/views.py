from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .models import skill, Contactinfo, Book
from .forms import Bookform

def home(request):
    item = skill.objects.all()

    title = "Welcome to mysite."

    desc = """This is a web site where you can upload or download required documents after logging in."""

    context = {
        
        'title' : title,
        'desc' : desc,
        'data' : item
    }


    return render(request,'index.html',context)

def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk = pk)
        book.delete()
    return redirect('books')

def profile(request):

    return render(request,'profile.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')



        #mydata = Contactinfo(cname = name, cemail = email, cquery = comments)
        mydata = Contactinfo()
        mydata.cname = name
        mydata.cemail = email
        mydata.cquery = comments

        mydata.save()

    return render(request, 'contact.html')

def books(request):
    
    books = Book.objects.all()

    return render(request, 'books.html', {'books':books})


def upload_book(request):
    if request.method == 'POST':
        form = Bookform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = Bookform()
    return render(request,'upload_book.html', {'form':form})