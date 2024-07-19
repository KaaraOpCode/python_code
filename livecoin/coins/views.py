from django.shortcuts import render

def login(request):
    return render(request,'login.html',)

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def coins(request):
    return render(request, 'dashboard/coins.html')

def profile(request):
    return render(request, 'dashboard/profile.html')

def downliners(request):
    return render(request,'dashboard/downliners.html')            
 
def transactions(request):
    return render(request,'dashboard/transactions.html')            
# Create your views here.
