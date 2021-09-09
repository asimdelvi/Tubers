from django.http.response import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from contact.models import Hiretuber


# Create your views here.
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username = username, password = password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'User created successfully')
      return redirect('dashboard')
    else:
      messages.warning(request, 'Invalid credentials')
      return redirect('login')


  return render(request, 'accounts/login.html')


def logout_account(request):
  logout(request)
  return redirect('home')


def register(request):
  if request.method == "POST":
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password == confirm_password:
      if User.objects.filter(username= username).exists():
        messages.warning(request, 'username exists')
        return redirect('login')
      else:
        user = User.objects.create_user(first_name=firstname,
                                        last_name=lastname,
                                        username=username,
                                        email=email,
                                        password=password)
        user.save()
        messages.success(request, 'User created successfully')
        return redirect('login')
    else:
      messages.warning(request, 'password is not same as confirm password')
      return redirect('login')

  return render(request, 'accounts/register.html')

@login_required(login_url='login')
def dashboard(request):
  user_id = request.user.id
  requested_youtubers = Hiretuber.objects.filter(user_id = user_id)
  data = {
    'user_id': user_id,
    'requested_youtubers': requested_youtubers,
  }
  return render(request, 'accounts/dashboard.html', data)
