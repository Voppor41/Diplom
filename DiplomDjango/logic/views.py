from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_up(request):
    info = {}  # Пустой словарь для передачи контекста
    if request.method == 'POST':
        form = UserRegister(request.POST)  # Передаем список пользователей в форму
        if form.is_valid():
            user = form.save()
            return HttpResponse(f"Приветствуем, {user.username}!")
        else:
            # Если форма не прошла валидацию, выводим ошибки
            info['form'] = form  # Передаем форму с ошибками в шаблон
    else:
        form = UserRegister()  # Пустая форма

    info['form'] = form  # Передаем форму в шаблон
    return render(request, 'registration.html', info)