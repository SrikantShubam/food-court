from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import users

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm
# Create your views here.



# def f_sign_up(request):
# 	if request.user.is_authenticated:
# 		return redirect('/dishes')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('email')
# 				messages.success(request, 'Account was created for ' + user)
# 				# Name = request.POST["username"]
# 				Email = request.POST["email"]
# 				# Mobile_Number = request.POST["phone"]
# 				# Password = request.POST.get("confirm_password", False)

# 				sign_up_data = f_users()
# 				# sign_up_data.user_Id = Name
# 				sign_up_data.user_Email = Email
# 				# sign_up_data.mobile_number = Mobile_Number
# 				# sign_up_data.password = Password
# 				print("Form is not Saved")
# 				sign_up_data.save()
# 				print("Form Saved")

# 				return redirect('dishes:leaderboard')
			

# 		context = {'form':form}
# 		return render(request, 'signup.html', context)



def f_sign_up(request):
    if request.user.is_authenticated:
        return redirect('/dishes')
    else:
        if request.method == 'POST':
            if request.POST['nPassword1'].strip() == request.POST['nPassword2'].strip():
                user = User(password=make_password(request.POST['nPassword1'].strip()),
                            username=request.POST['nEmail'],
                            email=request.POST['nEmail'])
                user.save()
                # userdetails = f_users(user_name=user.username, email=user.email,
                #                           mobile_number=request.POST['nPhone'], user_id=user)
                userdetails = f_users(user_Id=user, user_Email=user.email)
                userdetails.save()
                return redirect('users:f_login')
            else:
                context = {
                    'msg': 'Error in the inputs given, kindly make sure that you are using proper details to create user'
                }
                return render(request, 'signup.html', context)
        context = {
            'msg': ''
        }
        return render(request, 'signup.html', context)


def f_login(request):
	if request.user.is_authenticated:
		return redirect('/dishes')
	else:
		if request.method == 'POST':
			# Email = request.POST.get('email_address')
			Email = request.POST.get('email_address')
			password =request.POST.get('password')


			print(Email)
			print(password)

			user = authenticate(request, username=Email, password=password)

			if user is not None:
				print("Login success")
				login(request, user)
				request.session["login_status"]=True
				request.session["user_email"]=user.email
				print(request.session["user_email"])
				if 'next' in request.POST:
					return redirect(request.POST.get('next'))
				elif user.is_staff == 1:
					return redirect('main:admin_dashboard')
				else:
					return redirect('dishes:leaderboard')
			else:
				print('Login is not success')
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/login')