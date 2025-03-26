from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 올바른 값은 그대로 유지
            form.save()
            return redirect('accounts:login')
    else:
        form= CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)