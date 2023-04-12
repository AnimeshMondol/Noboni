from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, DoctorAccountAuthenticationForm, DoctorRegistrationForm


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('login')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def doc_reg_view(request):
	context = {}
	if request.POST:
		form = DoctorRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('doctor_login')
		else:
			context['registration_form'] = form

	else:
		form = DoctorRegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/doctor_register.html', context)


def logout_view(request):
	logout(request)
	return redirect('home')


def login_view(request):

	context = {}

	user = request.user
	

	if request.POST:
		form = 	AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("index")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)	



def doc_login_view(request):

	context = {}

	user = request.user
	

	if request.POST:
		form = 	DoctorAccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			lcno = request.POST['lcno']
			user = authenticate(email=email, password=password, lcno=lcno)

			if user:
				login(request, user)
				return redirect("doctor_index")

	else:
		form = DoctorAccountAuthenticationForm()

	context['doctor_login_form'] = form

	# print(form)
	return render(request, "account/doctor_login.html", context)	