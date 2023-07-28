from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from contactformapp import contactform, models
from django.template import loader
from django.core.mail import send_mail

# Create your views here.
'''
def register(request):
    register_form = contactform.RegistrationForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid(): 
            #userobj = register_form.save()
            # login(request, userobj)
            #return HttpResponseRedirect('/thanks/')
            new_user = models.User.objects.create_user(username=register_form.cleaned_data['username'],
                                                       email=register_form.cleaned_data['email'],
                                                       password=request.POST['password1'])
            new_user.is_active = False
            new_user.save()
            return redirect('/')
            # return HttpResponseRedirect(reverse('index'))
    return render(request, 'registrationform.html', {'form': register_form})

'''

def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def signup(request):
    template = loader.get_template("signup.html")
    context = {}
    return HttpResponse(template.render(context, request))

def thanks(request):
    template = loader.get_template("thanks.html")
    context = {}
    return HttpResponse(template.render(context, request))

#
# def contactus(request):
#
#     if request.method == "POST":
#         form = contactform.contactus(request.POST)
#         if(form.is_valid()):
#             form.save()
#             # send mail to itsmepriyap
#
#             send_mail(
#                 "User Feedback",
#                 "Here is the message.",
#                 "from@example.com",
#                 ["to@example.com"],
#                 fail_silently=False,
#             )
#             return HttpResponseRedirect("/thanks", request)
#             # return HttpResponse("success")
#             # return redirect('/')
#     else:
#         form = contactform.registerform()
#         return render(request, "contact.html", {'form': form})
