from django.shortcuts import render
from django.views import View


# Create your views here.
class RegistrationView(View):
    @staticmethod
    def get(request):
        return render(request, 'authentication/register.html')
