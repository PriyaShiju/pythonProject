from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, get_connection
from django.core import mail
import smtplib
# from contactformapp.models import contactus


attrs_d = {'class': 'required'}


class registerform(forms.Form):
    name = forms.RegexField(regex=r'^\w+$', max_length=30, widget=forms.TextInput(attrs=attrs_d), label='username')
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs_d), label='email address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_d, render_value=False), label='password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_d, render_value=False), label='password (again)')

def register(request):
    registered = False
    if request.method == "POST":
        form = contactusform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                ['User Registration'],
                ['Successfully Registered with DevOps Free Mocks Tests'],
                cd.get('email', 'noreply@example.com'),
                ['itsmepriyap@gmail.com'],
                connection=con
            )
            # return HttpResponseRedirect("/contactus?registered=True")
            return HttpResponseRedirect("/thanks", request)
            # return HttpResponse("success")
            # return redirect('/')
    else:
        form = contactusform()
        if 'registered' in request.GET:
            registered = True

    return render(request, "contact.html", {'form': form, 'registered': registered})


attrs_dict = {'class': 'form-control'}


class contactusform(forms.Form):
    name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs=attrs_dict))
    emailid = forms.EmailField(label='Email Address', max_length=50, widget=forms.TextInput(attrs=attrs_dict))
    subject = forms.CharField(max_length=500, widget=forms.TextInput(attrs=attrs_dict))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs=attrs_dict))


def contactus(request):
    submitted = False
    if request.method == "POST":
        form = contactusform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # server = smtplib.SMTP('smtp.gmail.com',587)
            # server.ehlo()
            # server.starttls()
            # server.login('itsmepriyap@gmail.com','pwd')
            # server.sendmail(cd.get('email', 'noreply@example.com'), ['itsmepriyap@gmail.com'],cd['message'])
            # server.quit()
            with mail.get_connection() as con:
                mail.EmailMessage(
                    cd['subject'],
                    cd['message'],
                    cd['emailid'],
                    ['itsmepriyap@gmail.com'],
                    connection=con,
                ).send()

            # con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd['emailid'], #.get('email', 'noreply@example.com'),
            #     ['itsmepriyap@gmail.com'],
            #     connection=con
            # )
            return HttpResponseRedirect("/contactus?submitted=True")
            # return HttpResponseRedirect("/thanks", request)
            # return HttpResponse("success")
            # return redirect('/')
    else:
        form = contactusform()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "contact.html", {'form': form, 'submitted': submitted})
