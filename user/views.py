from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('myapp:products')

    form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


@login_required
def profile(request):
    return render(request, 'user/profile.html')


def createprofile(request):

    if request.method == "POST":
        phone = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(user=user, image=image, phone=phone)
        profile.save()

    return render(request, 'user/createprofile.html')


def sellerprofile(request, id):
    seller = User.objects.get(id=id)
    context = {
        'seller': seller
    }
    return render(request, 'user/sellerprofile.html', context)
