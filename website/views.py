from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views import generic
from mainapp import settings
from .models import Category, Post, SiteProfile

# navbar_catgories = Category.objects.all().values('id','name',)

# Create your views here.
def index(request):
    
     return render(request, 'index.html')
 

def about(request):
    template_name = 'about.html'
    queryset = Post.objects.filter(is_about=1)    
    context ={'queryset': queryset}    
    return render(request, template_name, context)

def postdetail(request, slug, pk):
    template_name = 'post_detail.html'
    queryset = Post.objects.filter(id=pk)
    next_post = Post.objects.filter(is_about=0).filter(id=(pk+1)).values('pk','title','slug')
    previous = Post.objects.filter(is_about=0).filter(id=(pk-1)).values('pk','title','slug')    
    context ={'queryset': queryset, 
              'next': next_post, 
              'previous': previous,               
              }    
    return render(request, template_name, context)

def search(request): 
    template_name = 'search.html'    
    if request.method == "POST":                
        query = request.POST.get('searched')
        queryset = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
            ).distinct()
    context = {'searched': queryset, 
               'query':query,               
               }    
    return render(request,
            template_name,
            context)
        
def PostCategoryList(request,slug, pk):    
    template_name = "category.html" 
    queryset = Post.objects.defer('content').filter(status=1).filter(is_about=0).filter(categories=pk).order_by('-created_on')
    catname = Category.objects.filter(id=pk).values('name')   
    context = {'queryset': queryset, 'slug': slug, 'catname' : catname }    
    return render(request,template_name,context)


class PostList(generic.ListView):
    queryset = Post.objects.defer('content').filter(status=1).filter(is_about=0).order_by('-created_on')
    template_name = 'post_list.html'
    paginate_by = 5

# changed to a fuction call to allow for pagination
# remove at a later date when you are certain that you no longer need to reference this
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
    
    

    

