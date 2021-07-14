from django.db import models
from django.contrib.auth.models import User

class job_exp_model(models.Model):
    start_time=models.CharField(max_length=4)
    end_time=models.CharField(max_length=8)
    work_field=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    dtails=models.TextField()

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.company_name



PROJECT_CHOICE=(
    ('webdevelopment','webdevelopment'),
    
)
class myprotfolio(models.Model):
    title=models.CharField(max_length=100)
    pimage=models.ImageField(upload_to='protfolio')
    category=models.CharField(choices=PROJECT_CHOICE,max_length=50)
    code_link=models.TextField()

    class Meta:
        ordering=['-id']
    
    def __str__(self):
        return self.title

    
class dtailprotfolio(models.Model):
    #OneToOne
    project=models.OneToOneField(myprotfolio,on_delete=models.CASCADE)
    img1=models.ImageField(blank=True ,upload_to='dtail_protfolio')
    img2=models.ImageField(blank=True,upload_to='dtail_protfolio')
    img3=models.ImageField(blank=True,upload_to='dtail_protfolio')
    img4=models.ImageField(blank=True,upload_to='dtail_protfolio')
    img5=models.ImageField(blank=True,upload_to='dtail_protfolio')
    img6=models.ImageField(blank=True,upload_to='dtail_protfolio')
    img7=models.ImageField(blank=True,upload_to='dtail_protfolio')
    img8=models.ImageField(blank=True,upload_to='dtail_protfolio')
    img9=models.ImageField(blank=True,upload_to='dtail_protfolio')
    img10=models.ImageField(blank=True,upload_to='dtail_protfolio')

    def __str__(self):
        return self.project.title
    

MARKET=(
    ('fiverr','fiverr'),
    ('freeencer','freeencer')
)
class review_model(models.Model): 
    name=models.CharField(max_length=150)
    image=models.ImageField(default='review/avatars.jpg', upload_to='review')
    discription=models.TextField()
    profession=models.CharField(max_length=150)
    catagory=models.CharField(choices=MARKET,max_length=100)

    def __str__(self):
        return self.name
    
class blog_class(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='blog')
    type=models.CharField(max_length=150)
    created=models.DateField(auto_now=True)
    discription=models.TextField()

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.title


    
    
  

    





