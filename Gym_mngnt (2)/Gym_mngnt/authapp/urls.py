from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    path('trainer_reg',views.trainer_reg,name="trainer_reg"),
    path('t_reg', views.t_reg, name="t_reg"),
    path('tutorial', views.tutorial, name="tutorial"),
    path('tutorial_paid', views.tutorial_paid, name="tutorial_paid"),
    path('suppliments', views.suppliments, name="suppliments"),
    path('about', views.about, name="about"),
    path('pay', views.pay, name="pay"),
    path('payment_page', views.payment_page, name="payment_page"),
    path('user_about', views.user_about, name="user_about"),
    path('user_contact', views.user_contact, name="user_contact"),
    path('user_con', views.user_con, name="user_con"),

    path('tutorial_video', views.tutorial_video, name="tutorial_video"),
    path('add_to_paymnet_videos', views.add_to_paymnet_videos, name=""),
    path('checkout_session', views.checkout_session),
    path('pay_success', views.pay_success),
    path('view_video', views.view_videos),
    path('pay_failure',views.pay_failure),
    path('user_profile', views.user_profile, name="user_profile"),
    path('update_profile', views.update_profile),

    path('attendence_details', views.attendence_details, name="attendence_details"),


    
]
