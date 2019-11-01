from django.shortcuts import render,redirect
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
        return redirect('landingpage:done')
    else:
        return render(request, 'landingpage/beta.html')

def done(request):
    return render(request, 'landingpage/done.html')
