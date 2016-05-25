from django.shortcuts import redirect

def logout(request):
    logout(request)
    redirect('login')