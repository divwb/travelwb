from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm, CustomerProfileForm, BookingForm
from .models import Places, Customer
from django. core.paginator import Paginator,EmptyPage,InvalidPage



# Create your views here.
def home(request):
    place=Places.objects.all()
    paginator=Paginator(place,5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        place = paginator.page(page)
    except(EmptyPage, InvalidPage):
        place = paginator.page(page)
    return render(request,'home.html',locals())

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

class PlacesView(View):
    def get(self,request,val):
        place=Places.objects.filter(place=val)
        title=Places.objects.filter(place=val).values('title')
        return render(request,'place.html',locals())

class PlaceTitle(View):
    def get(self, request, val):
        place= Places.objects.filter(title=val)
        title=Places.objects.filter(place=place[0].place).values('title')
        return render(request,"place.html",locals())

class PlaceDetail(View):
    def get(self,request,pk):
        place=Places.objects.get(pk=pk)

        return render(request,'placedetail.html',locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'customerregistration.html',locals())

    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Registered Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'customerregistration.html',locals())


class BookingView(View):
    def get(self, request):
        form = BookingForm()
        return render(request,'bookingdetails.html', locals())

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request,'bookingdetails.html', locals())



class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'profile.html',locals())
    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']

            reg=Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'profile.html',locals())

def address(request):
     add=Customer.objects.filter(user=request.user)
     return render(request,'address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,'updateAddress.html',locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile Updated Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect('address')

def payment(request):
    return render(request,'payment.html')

def bookingsuccessful(request):
    return render(request,'bookingsuccessful.html')


def search(request):
    query = None
    place = None
    if 'q' in request.GET:
        query=request.GET.get('q')
        place=Places.objects.all().filter(Q(title__contains=query)|Q(description__contains=query))
    return render(request,'search.html', locals())