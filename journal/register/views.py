from django.shortcuts import render, redirect
from .forms import UserReg, ImageChange, UserChange
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        new_user_f = UserReg(request.POST)
        if new_user_f.is_valid():
            new_user_f.save()
            name = new_user_f.cleaned_data.get('username')
            messages.success(request, f'Пользователь {name} успешно зарегистрирован')
            return redirect('home')
    else:
        new_user_f = UserReg()
    d = {'form': new_user_f}
    return render(request, 'register/reg.html', d)


@login_required()
def profile(request):
    if request.method == 'POST':
        img_change = ImageChange(request.POST, request.FILES, instance=request.user.profile)
        user_change = UserChange(request.POST, instance=request.user)
        if img_change.is_valid() and user_change.is_valid():
            img_change.save()
            user_change.save()
            messages.success(request, "Изменения успешно сохранены")
    else:
        img_change = ImageChange(instance=request.user.profile)
        user_change = UserChange(instance=request.user)
    d = {
        'img_change_f': img_change,
        'user_change_f': user_change
    }
    return render(request, "register/profile.html", d)