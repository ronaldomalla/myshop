
#Authentication
from django.contrib.auth import authenticate

#Shortcuts
from django.shortcuts import render,redirect


# ============Models================
from .models import Products
from .models import Category
from .models import Customer


# Measage Framwork
from django.contrib import messages


# ==========Password Hashing==========
from django.contrib.auth.hashers import make_password,check_password


from django.views import View


# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    

    def post(self,request):
        email=request.POST['email']
        password=request.POST['password']
        customer = Customer.get_customer_by_email(email)
        if customer:
             flag=check_password(password,customer.password)
             if flag:
                 request.session['customer']=customer.id 
                 request.session['email']=customer.email
                 return redirect('home')
             else:
                 
                 error_message='Invalid Email or Password'
                        
        else:
             error_message='Invalid Email or Password'
        return render(request,'login.html',{'error':error_message})



class Signup(View):


    def validate(self,customer):

        Validate=None
        Email_Already_In_Use=customer.Already_Exists()
        if not customer.firstname:
            Validate='First name required'
        elif customer.firstname:
            if len(customer.firstname)<4:
                Validate='FirstName must be atleast 4 Chracters'
        elif not customer.lastname:
            Validate='Last Name Required' 
        elif customer.lastname: 
            if len(customer.lastname)<4:
                Validate='LastName must be atleast 4 Characters'
        elif not customer.password:
            Validate='Passowrd Required'
        elif customer.password:
            if len(customer.password)<8:
                Validate='Password must be 8 Characters long'    
        elif not customer.phone:
            Validate='Phone Number Required'   
        
        elif Email_Already_In_Use:
            Validate='Email Already In Use Try Login Instead'
        return Validate
    
    
    
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        customer=Customer(firstname=firstname,lastname=lastname,email=email,password=password,phone=phone)
        value={
            'firstname':firstname,
            'lastname':lastname,
            'email':email,
            'phone':phone,
        }
        


        Validate=self.validate(customer)
        if not Validate:
         customer.password=make_password(customer.password)
         customer.save()
         messages.success(request,'Sign Up has been sucessfull')
         return redirect('home')
        
        else:
         data={
            'error':Validate,
            'value':value,
         }
         return render(request,'signup.html',data)













        Validate=None
        Email_Already_In_Use=customer.Already_Exists()
        if not customer.firstname:
            Validate='First name required'
        elif customer.firstname:
            if len(customer.firstname)<4:
                Validate='FirstName must be atleast 4 Chracters'
        elif not customer.lastname:
            Validate='Last Name Required'
        elif customer.lastname: 
            if len(customer.lastname)<4:
                Validate='LastName must be atleast 4 Characters'
        elif not customer.password:
            Validate='Passowrd Required'
        elif customer.password:
            if len(customer.password)<8:
                Validate='Password must be 8 Characters long'    
        elif not customer.phone:
            Validate='Phone Number Required'   
        
        elif Email_Already_In_Use:
            Validate='Email Already In Use Try Login Instead'
        return Validate
        


def index(request):
    cart=request.session.get('cart')
    product=request.POST.get('products_id')
    remove=request.POST.get('remove')
    if cart:
        quantity=cart.get(product)
        if quantity:
            if remove:
                cart[product]=quantity-1
            else:
                cart[product]= quantity+1
        else:
             cart[product]=1
    else:
        cart={}
        cart[product]=1


    request.session['cart']=cart
    print(cart)






    categories=Category.get_all_categories()
    categoryId=request.GET.get('category')
    if categoryId:
        products=Products.get_all_products_by_categoryId(categoryId)
    else:
        products=Products.get_all_products()
    data={}
    data['products']=products
    data['categories']=categories
    return render(request,'index.html',data)





        



         

            
             
        


        


    
def cart(request):
    ids=list(request.session.get('cart').keys())
    if ids:
          products=Products.get_products_by_id(ids)
    context={'products':products}
    
    return render(request,'cart.html',context)



def logout(request):
    request.session.clear()
    return redirect('home')