from django.shortcuts import render , HttpResponse ,redirect
from datetime import datetime
from .form import ImageForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from math import ceil

#  username : user2 password : password@123
#  username: user password : password@123




def index(request):


    product = Product.objects.all().reverse()
    print(product)
    n = len(product)
    slides = n//4+ceil((n/4)-(n//4))

    params ={'slides': slides,'range':range(1,slides),'product': product}

    return render(request,"index.html",params)





def usrin(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        upass = request.POST.get('password')

        user = authenticate(request, username=uname, password=upass)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            return render(request, "login.html", {'error': 'Invalid username or password'})

    return render(request, "login.html")




def usrout(request):
    logout(request)
    return render(request,"index.html")

def usrup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if len(password) < 8:
            error_message = 'Password should be at least 8 characters long.'
        elif password != confirm_password:
            error_message = 'Passwords do not match.'
        else:
            try:
                # Check if the username already exists
                existing_user = User.objects.get(username=username)
                if existing_user:
                    error_message = 'Username already exists. Please choose a different username.'

            except User.DoesNotExist:
                # Create the new user and save to the database
                user = User.objects.create_user(username=username, password=password, email=email,first_name=firstname,last_name=lastname)
                profile = UserProfile()
                profile.user = user
                profile.role = "buyer"
                profile.save()  # Save the UserProfile instance

                success_message = 'Account created successfully.'
                return render(request, 'login.html', {'success_message': success_message})
            
        return render(request, 'signup.html', {'error_message': error_message})
    
    return render(request, 'signup.html')


def cart(request):
    return render(request, 'cart.html')



def artgal(request):
    product = Product.objects.all()
    print(product)
    n = len(product)
    slides = n//4+ceil((n/4)-(n//4))
    params ={'slides': slides,'range':range(1,slides),'product': product}
    for product in product:
        print(product.price)
    return render(request,"artgal.html",params)



def upfedit(request):
    print(request)
    user_role = None
    if request.user.is_authenticated:
        # Retrieve the user's profile
        user_profile = request.user.userprofile

        # Access the role attribute
        user_role = user_profile.role
    return render(request, 'upfedit.html',{'user_role': user_role})



def uprod(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print("if case")
            obj = form.instance
            print("obj: ",obj)
            return render(request, "upload.html", {"obj": obj})
    else:
        print("else case ")
        form = ImageForm()
    img = Product.objects.all()
    print("img: ",img)
    return render(request, "upload.html", {"img": img, "form": form})


def checkout(request):
    return render(request,"checkout.html")

def blog(request):
    return render(request,"blog.html")

def checkout(request):
    if request.method=="POST":
        # print(request.POST.get())
        # items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('fname', '')
        amount = 11
        email = request.POST.get('email', '')
        address = request.POST.get('address', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        order = Orders( name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = UpdateOrder(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        return render(request, 'index.html')
    return render(request, 'checkout.html')


def contact(request):
     print("hello")
     if request.method=="POST":
        name = request.POST.get('name','')
        email=  request.POST.get('email','')
        phone =  request.POST.get('phone','')
        rest =  request.POST.get('rqst','')
        cont = Contact(name=name,email=email,phone=phone,rqst=rest)
        cont.save()
        print("yeah")
        return render(request,"contact.html")
     
     return render(request,"contact.html")
     
     


