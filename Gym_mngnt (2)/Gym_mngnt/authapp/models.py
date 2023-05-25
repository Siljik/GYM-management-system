from distutils.command.upload import upload
from django.db import models

# Create your models here.
# this file we creates a database tables

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self):
        return self.email

class Enrollment(models.Model):        
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    Address=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField()
    trainer_img = models.ImageField(upload_to='gallery',null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField()
    def __int__(self):
        return self.id


class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    # Login=models.CharField(max_length=200)
    # Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    def __int__(self):
        return self.id

class Suppliments(models.Model):
    item=models.CharField(max_length=200)
    image=models.FileField()
    price=models.IntegerField()
    details=models.CharField(max_length=200, null=True)
    def __int__(self):
        return self.id



class Payment_user(models.Model):
    card_no=models.CharField(max_length=20)
    card_date=models.CharField(max_length=20)
    card_cvv=models.CharField(max_length=20)
    card_name=models.CharField(max_length=30)
    status=models.BooleanField()
    card_mobile=models.CharField(max_length=30)
    def __int__(self):
        return self.id

class video_category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class videos(models.Model):
   
    video_title=models.CharField(max_length=100)
    category=models.ForeignKey(video_category,on_delete=models.CASCADE,null=True)
    video=models.FileField(upload_to='videos/')
    payment = models.IntegerField()
    def __str__(self):
        return self.video_title


class payment_videos(models.Model):
    user=models.CharField(max_length=100)
    video_title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    video=models.FileField(upload_to='videos/')
    payment = models.IntegerField()
    def __str__(self):
        return self.video_title


class view_video(models.Model):
    user=models.CharField(max_length=100)
    video_title=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    video=models.FileField(upload_to='videos/')
    def __str__(self):
        return self.video_title

class user_details(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    Address=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,)

    def __str__(self):
        return self.FullName


