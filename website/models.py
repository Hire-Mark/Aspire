from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField 
from django.urls import reverse
from phone_field import PhoneField
from mainapp.settings import AUTH_USER_MODEL

# CHOICE SECTION START
# used for choice statements in the model fields
YESNO = {
    (0,"No"),
    (1,"Yes")
}

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

SITE_STATUS = (
    (0,"Maintenance"),
    (1,"Production")
)

# CHOICE SECTION - END

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    navbar_main = models.IntegerField(choices=YESNO, default=1)
    navbar_footer = models.IntegerField(choices=YESNO, default=0)
    navbar_secondary = models.IntegerField(choices=YESNO, default=0)
    navbar_sidebar = models.IntegerField(choices=YESNO, default=0)
    active = models.IntegerField(choices=YESNO, default=1)
    header_image = models.ImageField( upload_to='images/', blank=True)
    seo = models.TextField(max_length=200, default='null')
    description = RichTextUploadingField(default='null') # CKEditor Rich Text Field
    
              
    def __str__(self):
        return self.name



class Post(models.Model):
    status = models.IntegerField(choices=STATUS, default=0)
    is_about = models.IntegerField(choices=YESNO, default=0)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.DO_NOTHING,related_name='blog_posts')
    header_image = models.ImageField( upload_to='posts/header_images', blank=True)
    categories = models.ManyToManyField(Category, default="1")
    updated_on = models.DateTimeField(auto_now= True)
    seo_teaser = models.TextField(max_length=200, default='NULL')
    content = RichTextUploadingField() # CKEditor Rich Text Field
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})


# model used to store site data
# accessed through context_processors.py
# model used to produce an about page

class SiteProfile(models.Model):
    number = models.IntegerField(unique=True)
    status = models.IntegerField(choices=SITE_STATUS, default=0)
    title = models.CharField(max_length=60, null=True, blank=True)
    slug = models.SlugField(max_length=60,null=True, blank=True)
    tagline = models.CharField(max_length=75, null=True, blank=True)
    logo = models.ImageField( upload_to='images/website', blank=True)    
    contact = models.CharField(max_length=35, null=True, blank=True)
    email = models.CharField(max_length=35, null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    website = models.CharField(max_length=35, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    address2 = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    google_map = models.CharField(max_length=200, null=True, blank=True)
    seo_description = models.CharField(max_length=200, null=True, blank=True)
    bio_title = models.CharField(max_length=60, null=True, blank=True)
    bio_slug = models.SlugField(max_length=60,null=True, blank=True)
    bio_tagline = models.CharField(max_length=75, null=True, blank=True)   
    bio_header = models.CharField(max_length=75, null=True, blank=True)  
    bio = RichTextUploadingField() # CKEditor Rich Text Field
    #social media profile links
    facebook = models.CharField(max_length=30, null=True, blank=True)
    linkedin = models.CharField(max_length=30, null=True, blank=True)
    twitter = models.CharField(max_length=30, null=True, blank=True)
    instagram = models.CharField(max_length=30, null=True, blank=True)
    tiktok = models.CharField(max_length=30, null=True, blank=True)
    google_profile = models.CharField(max_length=200, null=True, blank=True)    
    youtube = models.CharField(max_length=200, null=True, blank=True)
    cashapp = models.CharField(max_length=30, null=True, blank=True)
    venmo = models.CharField(max_length=30, null=True, blank=True)
    github = models.CharField(max_length=30, null=True, blank=True)
    discord = models.CharField(max_length=30, null=True, blank=True)
    linktree = models.CharField(max_length=30, null=True, blank=True)
    facetime = models.CharField(max_length=30, null=True, blank=True)
    microsoft = models.CharField(max_length=30, null=True, blank=True)
    twitch = models.CharField(max_length=30, null=True, blank=True)

    
    
    class Meta:
         verbose_name = "Site Profile"
    
    def __str__(self):
        return self.title 
    
    
