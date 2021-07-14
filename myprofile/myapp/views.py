from django.shortcuts import render
from .models import job_exp_model,myprotfolio,dtailprotfolio,review_model,blog_class
from django.core.paginator import Paginator


def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return render(request,'myapp/about.html')
def service(request):
    return render(request,'myapp/service.html')

def experience(request):
    job=job_exp_model.objects.all()
    dic={
        'jobs':job
    }
    return render(request,'myapp/experience.html',dic)


def portfolio(request):
    mp=myprotfolio.objects.all()
    dic={
      'mp':mp
    }
    return render(request,'myapp/portfolio.html',dic)

def dtailportfolio(request):
    pk=request.POST['projrct_id']  

    project_dtail=dtailprotfolio.objects.get(project=pk)
    cnt= 10 * 'a'

    # print('-------------',cnt)
    # print('-------------',project_dtail)

    dic={
        'pd':project_dtail,
        'cnt':cnt
    }
    return render(request,'myapp/dtailprotflio.html',dic)

def price(request):
    return render(request,'myapp/price.html')
# def team(request):
#     return render(request,'myapp/team.html')

def review(request):
    review=review_model.objects.all()
    dic={
       'review':review,
    }
    return render(request,'myapp/review.html',dic)


def contact(request):
    return render(request,'myapp/contact.html')


def blog(request):
    blog=blog_class.objects.all()

    p=Paginator(blog,2)
    page=request.GET.get('page')
    post_page=p.get_page(page)
    pg_nums= 'a' * post_page.paginator.num_pages
    dic={
       'post_page':post_page,
       'pg_nums':pg_nums,
    }
  
    return render(request,'myapp/blog.html',dic)

def dtail_blog(request):
    post_id=request.POST['post_id']
    post=blog_class.objects.get(id=post_id)
    dic={
        'post':post
    }
    return render(request,'myapp/dtail_post.html',dic)