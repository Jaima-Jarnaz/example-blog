from django.http import Http404
from django.views import View
from django.contrib.auth.hashers import check_password,make_password
from django.shortcuts import render,redirect
from .models import Customer 



def register(request):
    if request.method =='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        error_message=None
        if not firstname:
            error_message="Fill the first name"
        elif len(firstname)<5:
            error_message="Firstname must be longer than 4 character"
        elif not lastname:
            error_message="Fill the last name"
        elif len(password)<6:
            error_message="Password lenght must be atleast 7"
        elif Customer.objects.filter(email=email):
            error_message="Email address already exists"
        elif password!=confirmpassword:
             error_message="Password not matched"
               
            
        if not error_message:
            password=make_password(password)
            confirmpassword=make_password(confirmpassword)
            customerlist=Customer( firstname=firstname,lastname=lastname ,email=email, password=password,confirmpassword=confirmpassword)
            customerlist.save()
            return redirect('/')
        else:    
            values={
            'error': error_message,
            'firstname':firstname,
            'lastname': lastname,
            'email': email,
            }
            return render(request,'register.html',values)

    else:
        return render(request,'register.html')



# LOGIN VIEW ENDPOINT
def match_customer(email):
    try:
        return Customer.objects.get(email=email)
    except:
        return False


class Login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        find_customer=match_customer(email)
        #data_error=None
        if find_customer:
            print(find_customer.password)
            print(password)
            match_password= check_password(password,find_customer.password)
            print(match_password)
            if match_password:
               request.session['customer_id']=find_customer.id 
               request.session['email']=find_customer.email
               return redirect('/')
            else:
                data_error="Email or password not matched"
                return render(request,'login.html', { 'error':data_error })
        else:
            data_error="Email or password not matched"
            return render(request,'login.html', { 'error':data_error })