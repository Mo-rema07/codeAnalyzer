from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserInputForm


@login_required
def user_input(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = UserInputForm()
    return render(request, 'upload.html', {'form': form})
