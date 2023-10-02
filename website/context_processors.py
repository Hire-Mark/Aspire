from asyncio.windows_events import NULL
from .models import Category, Post, SiteProfile
from django.db import connection

from django.db.models import Q


def site_settings(request):    
    queryset = SiteProfile.objects.all().filter(pk=1)

    print(queryset)
    
    if not queryset:
        title = 'Welcome to your new Aspire Blog'
        slug = 'Aspire-Blog'
        tagline = 'Made with Hart'
        logopath = 'themes/aspire/images/logo.png'
        copyright = '2023 copyright text'
        contact = 'Contact Name'
        email = 'contact email'
        phone = '555.555.5555'
        website = 'www.hire-mark.com'
        address = 'address 1'
        address2 = 'address 2'
        city = 'city'
        state = 'state'
        zip = 'zip'
        seo_description = 'Welcome to the Aspire, a simple user friendly custom CMS designed to meet your business needs'
        bio = 'This is your bio page'
        facebook = 'facebook'
        linkedin = 'linkedin'
        twitter = 'twitter'
        instagram = 'instagram'
        tiktok = 'tiktok'
        google = 'google_profile'
        cashapp = 'cashapp'
        youtube = 'youtube'
        venmo = 'venmo'
        discord = 'discord'
        github = 'github'
        microsoft = 'microsoft'
        github = 'github'
        linktree = 'linktree'
        twitch = 'twitch'
    else:
        for x in queryset:
            title = x.title
            slug = x.slug
            tagline = x.tagline
            logopath = x.logo
            contact = x.contact
            copyright = x.copyright
            email = x.email
            phone = x.phone
            website = x.website
            address = x.address
            address2 = x.address2
            city = x.city
            state = x.state
            zip = x.zip
            seo_description = x.seo_description
            bio = x.bio
            facebook = x.facebook
            linkedin = x.linkedin
            twitter = x.twitter
            instagram = x.instagram
            tiktok = x.tiktok
            google = x.google_profile
            cashapp = x.cashapp
            youtube = x.youtube
            venmo = x.venmo
            discord = x.discord
            github = x.github
            microsoft = x.microsoft
            github = x.github
            linktree = x.linktree
            twitch = x.twitch
    
    
    return {'title': title,
            'slug':slug,
            'tagline': tagline,
            'logo': logopath,
            'contact': contact,
            'copyright': copyright,
            'email': email,
            'phone': phone,
            'website': website,
            'address': address,
            'address2': address2,
            'city': city,
            'state': state,
            'zip': zip,
            'seo_description': seo_description,
            'bio': bio,
            'facebook': facebook,
            'linkedin': linkedin,
            'twitter': twitter,
            'instagram': instagram,
            'tiktok': tiktok,
            'google': google, 
            'youtube': youtube,
            'discord': discord,
            'venmo': venmo,
            'linktree': linktree,
            'cashapp': cashapp,
            'github':github,
            'microsoft': microsoft,
            'twitch': twitch                       
                }
    
    
def CategoryList(request):
    queryset = Category.objects.all().values('pk','name','slug')
    #print(queryset)
    return {'Categories': queryset }  

def navbar_main(request):
    queryset = Category.objects.all().values('pk','name','slug').filter(navbar_main=1)
    #print(queryset)
    return {'navbar_header': queryset }

def navbar_footer(request):
    queryset = Category.objects.all().values('pk','name','slug').filter(navbar_footer=1)
    #print(queryset)
    return {'navbar_footer': queryset }