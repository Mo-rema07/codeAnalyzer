from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from analyser.analyse import analyse
from analyser.readFromFile import handle_uploaded_file
from .forms import CodeSnippetForm, UploadFileForm


@login_required
def code_snippet(request):
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            code = form['code'].value()
            report = analyse(code)
            return render(request, 'feedback.html', {'report': report})
    else:
        return HttpResponseRedirect('')


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            code = handle_uploaded_file(request.FILES['file'])
            report = analyse(code)
            return render(request, 'feedback.html', {'report': report})
    else:
        return HttpResponseRedirect('')


@login_required
def home(request):

    snippet_form = CodeSnippetForm()
    upload_form = UploadFileForm()
    return render(request, 'upload.html', {
        'snippet_form': snippet_form,
        'upload_form': upload_form
    })
