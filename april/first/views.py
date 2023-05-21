from django.shortcuts import render, redirect
from . models import Author
from .forms import AuthorForm
# Create your views here.


def index(request):
    author = Author.objects.all()
    context = {
        'author': author
    }
    return render(request, 'index.html', context)


# for the pages without datasets

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def author(request):
    author = Author.objects.all()
    context = {
        'author': author
    }
    return render(request, 'author.html', context)


def createauthor(request):
    if request.method == "GET":
        authorform = AuthorForm
        return render(request, 'createauthor.html', context={'form': authorform})
    else:
        authorform = AuthorForm(request.POST, request.FILES)
        if authorform.is_valid():
            authorform.save()
            return redirect('index')
        return render(request, 'createauthor.html', context={'form': authorform})


def readauthor(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        'author': author

    }

    return render(request, 'readauthor.html', context)


def editauthor(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == "POST":
        form = AuthorForm(instance=author)
        form = AuthorForm(request.POST, instance= author)
        if form.is_valid():
            form.save()
            return redirect('author')
    else:
        form = AuthorForm(instance= author)
    return render(request, 'editauthor.html', context={'form': form, 'author': author})


def deleteauthor(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == "POST":
        return redirect('author')
    else:
        return render(request, 'deleteauthor.html', {'author': author})
