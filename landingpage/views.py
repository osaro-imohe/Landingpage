from django.shortcuts import render
from landingpage.models import Email

def home(request):
    return render(request,'landingpage/home.html')

def pricing(request):
    return render(request, 'landingpage/pricing.html')

def beta(request):
    if request.method == "POST":
        email = request.POST.get("email")
        detail = Email(useremail = email,)
        detail.save()
        print(email)
        return render(request, 'landingpage/beta.html')
    else:
        return render(request, 'landingpage/beta.html')
