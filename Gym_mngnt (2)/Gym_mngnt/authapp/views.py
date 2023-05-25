from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
# from Gym_mngnt.authapp.models import*


def Home(request):
    c = video_category.objects.all()
    context = {'c': c}
    return render(request,"index.html", context)



def user_about(request):
    trainer = Trainer.objects.all()
    context = {"c": trainer}
    return render(request,"user_about.html",context)

def user_con(request):
    return render(request, "user_con.html")
def user_contact(request):
    return render(request, "user_contact.html")

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        user_phone = request.user
        # phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=user_phone,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect(attendence_details)
    return render(request,"attendance.html",context)





def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')
        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass
        p = user_details(Email=email, PhoneNumber=username)
        p.save()
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
    return render(request,"signup.html")




def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        #pay_details=Payment_user.objects.all()
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            x=Payment_user.objects.filter(card_mobile=username)
            # print(x)
            if x:
                for i in x:
                    if i.status ==1:
                        # request.session['']=
                        return redirect('tutorial_paid')
                    else:
                        return redirect('tutorial')
            messages.success(request, "Login Successfully")
            return redirect('tutorial')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')


def user_con(request):
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        number = request.POST.get('num')
        desc = request.POST.get('desc')
        myquery = Contact(name=name, email=email, phonenumber=number, description=desc)
        myquery.save()
        return redirect(tutorial)
    return render(request, "tutorial.html")


def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")

def enroll(request):
    return render(request, "enroll.html")
def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        user_phone = request.user
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=user_phone
        DOB=request.POST.get('DOB')

        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/profile')
    return render(request,"update_profile.html",context)


def trainer_reg(request):
    return render(request, "trainer_regi.html")

def t_reg(request):
    FullName = request.POST.get('FullName')
    gender = request.POST.get('gender')
    PhoneNumber = request.POST.get('PhoneNumber')
    salary=request.POST.get('salary')
    t=Trainer(name = FullName,gender=gender,phone=PhoneNumber,salary=salary)
    t.save()
    messages.success(request, "Successfully registred")

    return redirect('/')
#########################################################
def tutorial(request):
    c = video_category.objects.all()
    context = {'c': c}
    return render(request,'tutorial.html', context)

def tutorial_paid(request):
    return render(request,'tutorial_paid.html')

def tutorial_video(request):
    id = request.GET.get("id")
    c = videos.objects.filter(category=id)
    context= {'videos': c}
    user = request.user
    print(user)
    return render(request,'tutorial_video.html', context)

def add_to_paymnet_videos(request):
    if request.method=="POST":
        v_title=request.POST.get('v_title')
        video=request.POST.get('video')
        category=request.POST.get('category')
        payment =request.POST.get('price')
        user = request.user
        print(user)
        p = payment_videos(user=user, video_title=v_title, video=video, category=category,payment=payment)
        p.save()
        request.session['payment_video_id']=p.id
        return render(request,'confirm_payment.html')
    else:
        return render(request,'tutorials_paid.html')


import stripe

stripe.api_key = 'sk_test_51MzR0qSDsHoB6h4XS89hryuFO2ZLs4EGe6bs44P45Pq1pYzw1FbxRGwfHU1kcz13dX9qi9RFj2PDlFn56vF51rOe00Stz4HfFt'

def checkout_session(request):
    cart_id = request.session['payment_video_id']
    cart_obj = payment_videos.objects.get(id=cart_id)

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': cart_obj.video_title,
                },
                'unit_amount': cart_obj.payment * 100,
            },
            'quantity': 1,
        }],

        mode='payment',
        success_url='http://127.0.0.1:8000/pay_success',
        cancel_url='http://127.0.0.1:8000/pay_failure',
    )
    # c = payment_videos.objects.get(id=cart_id)
    # v = videos.objects.get(video_title=c)
    # v.delete()
    return redirect(session.url, code=303)

def pay_success(request):
    v = request.session['payment_video_id']
    view = payment_videos.objects.filter(id=v)
    for i in view:
        v_title = i.video_title
        user=i.user
        category=i.category
        video=i.video
        view = view_video(user=user, video_title=v_title, category=category, video=video) 
        view.save()
    view_v = view_video.objects.all()    
    context = {'video': view_v}    
    return redirect(view_videos)

def view_videos(request):
    view = view_video.objects.filter(user=request.user)
    context = {'video': view}    
    return render(request,'view_video.html', context)  
  
def pay_failure(request):
    return render(request,'pay_failure.html')  

def confirm_payment(request):
    return render(request,'confirm_payment.html')




def suppliments(request):
    sup_list=Suppliments.objects.all()
    return render(request,"suppliments.html",{"key":sup_list})

def about(request):
    return render(request,"about.html")
def pay(request):
    no = request.POST.get('card_no')
    date = request.POST.get('card_date')
    cvv = request.POST.get('card_cvv')
    name = request.POST.get('card_name')
    mobile = request.POST.get('card_mobile')
    t = Payment_user(card_no=no, card_date=date, card_cvv=cvv, card_name=name,card_mobile=mobile,status=0)
    t.save()
    messages.success(request, "Waiting for approval,please login again")
    return render(request, 'payment.html')

def payment_page(request):
    return render(request, 'payment.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def attendence_details(request):
    user_phone = request.user
    attendance = Attendance.objects.filter(phonenumber=user_phone)
    context = { "attendance": attendance}
    return render(request, 'attendence_details.html', context)


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=user_details.objects.filter(PhoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)

def update_profile(request):
    if request.method == "POST":
        user_ph= request.user
        posts = user_details.objects.get(PhoneNumber=user_ph)
        f= request.POST.get('fname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        # PhoneNumber = user_ph
        DOB = request.POST.get('DOB')
        address = request.POST.get('address')

        posts.FullName = f
        posts.Email = email
        posts.Gender = gender
        posts.DOB = DOB
        posts.Address = address
        posts.save()
        return redirect('/profile')
    else:
        user_phone = request.user
        posts = user_details.objects.filter(PhoneNumber=user_phone)
        context = {"posts": posts}
    return render(request, "update_profile.html", context)
