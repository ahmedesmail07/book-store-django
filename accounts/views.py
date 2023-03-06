# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views import generic
# from .forms import CustomUserCreationForm  # The Customized form i did firstly


# class SignupPageView(generic.CreateView):
#     form_class = CustomUserCreationForm  # this my own customized form
#     success_url = reverse_lazy("login")  # befor URLconf is loaded
#     template_name = "registration/signup.html"  # redirct to this form page

# Thank to our allauth app it is easy way to make a register form without any issues
