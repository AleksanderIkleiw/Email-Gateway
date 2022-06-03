from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm, SendEmailForm
from django.contrib.auth import authenticate, login
from .mails import send_email

# Create your views here.


def home_view(request):
    print(f'Logged in as {request.user.username}')
    if request.method == 'POST':
        form = SendEmailForm(data=request.POST)
        if form.is_valid():
            success_messages = []
            errors_to_context = []
            print('ok')
            print(request.POST)
            to = form.cleaned_data.get('to')
            subject = form.cleaned_data.get('subject')
            text = form.cleaned_data.get('content')
            print(to, subject, text)
            if request.user.is_authenticated:
                response = send_email(to, subject, text)
                if response:
                    success_messages.append(f'Mail has been successfully sent to {to}')
                else:
                    errors_to_context.append('Something went wrong. Please try again.')

            else:
                errors_to_context.append('You have to be logged in order to use Email Gateway')
        else:
            print('nie ok')
            print(request.POST)
            errors = []
            errors_to_context = []
            success_messages = []
            for error in form.errors.keys():
                errors.append(form.errors[error])
            for error in errors:
                errors_to_context.extend(error)
    else:
        form = SendEmailForm()
        errors_to_context = []
        success_messages = []

    return render(request, 'login_system/home.html', context={'form': form,
                                                              'errors': errors_to_context,
                                                              'success': success_messages},)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered!')
            print('ok')
            return redirect('login_page')
        else:
            errors = []
            errors_to_context = []
            for error in form.errors.keys():
                errors.append(form.errors[error])
            for error in errors:
                errors_to_context.extend(error)

    else:
        form = RegisterForm()
        errors_to_context = []
    return render(request, 'login_system/register.html', {'register_form': form,
                                                          'errors': errors_to_context})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
            return redirect('home_page')
        else:
            errors = form.errors.get_json_data()['__all__']
    else:
        form = LoginForm()
        errors = []
    return render(request, 'login_system/login.html', {'form': form,
                                                       'errors': [error['message'] for error in errors]})
