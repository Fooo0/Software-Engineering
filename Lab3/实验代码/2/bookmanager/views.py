# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponseRedirect
from bookmanager.models import Book, Author
from bookmanager.forms import Form_Book_new, Form_Book_update, Form_Author

def Option(request):
    return render_to_response('option.html')

def Addbook(request):
    error = []
    if request.method == 'POST':
        bf = Form_Book_new(request.POST)
        if bf.is_valid():
            bf_clean = bf.cleaned_data
            title = bf_clean['Title']
            exit_book = Book.objects.filter(Title__exact = title)
            if exit_book:
                 error.append('该书已存在')
                 return render_to_response('editbook.html', locals())
            author_id = bf_clean['AuthorID']
            exit_author = Author.objects.filter(AuthorID__exact = author_id)
            if not exit_author:
                error.append('该作者不存在，请先添加新作者')
                return render_to_response('editbook.html', locals())
            bf.save()
            return HttpResponseRedirect('/option/')
        else:
            return render_to_response('editbook.html', locals())
    else:
        bf = Form_Book_new()
        return render_to_response('editbook.html', locals())

def Updatebook(request, book_pk):
    error = []
    book = Book.objects.filter(ISBN__exact = book_pk)[0]
    if request.method == 'POST':
        bf = Form_Book_update(request.POST, instance = book)
        if bf.is_valid():
            bf_clean = bf.cleaned_data
            author_id = bf_clean['AuthorID']
            exit_author = Author.objects.filter(AuthorID__exact = author_id)
            if not exit_author:
                error.append('该作者不存在，请先添加新作者')
                return render_to_response('editbook.html', locals())
            bf.save()
            return HttpResponseRedirect('/option/')
        else:
            return render_to_response('editbook.html', locals())
    else:
        bf = Form_Book_update(instance = book)
        return render_to_response('editbook.html', locals())

def Addauthor(request):
	error = []
	if request.method == 'POST':
		af = Form_Author(request.POST)
		if af.is_valid():
			af_clean = af.cleaned_data
			Name = af_clean['Name']
			exit_author = Author.objects.filter(Name__exact = Name)
			if exit_author:
				error.append('该作者已存在')
				return render_to_response('addauthor.html', locals())
			author = Author.objects.create(Name = Name, Age = af_clean['Age'],
				Country = af_clean['Country'])
			author.save()
			return HttpResponseRedirect('/option/')
		else:
			return render_to_response('addauthor.html', locals())
	else:
		af = Form_Author()
		return render_to_response('addauthor.html', locals())

def CheckauthorID(request):
    authors = Author.objects.all()
    return render_to_response('checkauthorID.html', locals())

def Search(request):
	errors = []
	message = []
	if 'author_name' in request.GET:
		author_name = request.GET['author_name']
		if not author_name:
			errors.append('请输入作者')
			return render_to_response('search.html', locals())
		else:
			author = Author.objects.filter(Name__exact = author_name)
			if not author:
				message.append('该作者不存在')
				return render_to_response('search_result.html', locals())
			author_pk = author[0].AuthorID
			books = Book.objects.filter(AuthorID__exact = author_pk)
			return render_to_response('search_result.html', locals())
	else:
		return render_to_response('search.html', locals())

def Detail(request, book_pk):
	errors = []
	book = Book.objects.filter(ISBN__exact = int(book_pk))[0]
	author_pk = book.AuthorID
	author = Author.objects.filter(AuthorID__exact = author_pk)[0]
	return render_to_response('detail.html', locals())

def Delete(request, book_pk, author_pk):
	book = Book.objects.filter(ISBN__exact = int(book_pk))[0]
	book.delete()
	books = Book.objects.filter(AuthorID__exact = author_pk)
	return render_to_response('search_result.html', locals())
