from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings  
from django.shortcuts import redirect
from .models import Slider, Category, SocialLink, SiteAddress, About, WhyChooseUs, Enquery, CoreValue, PostDetail, OurSkill

def index(request):
    all_slider = Slider.objects.all()
    all_about = About.objects.all()
    all_category = Category.objects.all()
    all_social = SocialLink.objects.all()
    all_address = SiteAddress.objects.all()
    all_whychoose = WhyChooseUs.objects.all()
    all_skill = OurSkill.objects.all()
    return render(request, 'index.html', { 'slider':all_slider,
                                           'about':all_about,
                                           'category':all_category,
                                           'social':all_social,
                                           'address':all_address,
                                           'whychoose':all_whychoose,
                                           'our_skill':all_skill,
                                         }) 

def about(request):
    all_about = About.objects.all()
    all_core = CoreValue.objects.all()
    all_category = Category.objects.all()
    all_social = SocialLink.objects.all()
    all_address = SiteAddress.objects.all()
    return render(request, 'about.html',{
                                         'about':all_about,
                                         'core':all_core,
                                         'category':all_category,
                                         'social':all_social,
                                         'address':all_address,
                                         })

def contact(request):
    all_category = Category.objects.all()
    all_social = SocialLink.objects.all()
    all_address = SiteAddress.objects.all()
    return render(request, 'contact.html',{
                                           'category':all_category,
                                           'social':all_social,
                                           'address':all_address,
                                           })

def details(request, cat_id):
    service_detail = PostDetail.objects.filter(category=cat_id)
    all_category = Category.objects.all()
    all_social = SocialLink.objects.all()
    all_address = SiteAddress.objects.all()
    return render(request, 'details.html', {
                                                    'detail':service_detail,
                                                    'category':all_category,
                                                    'social':all_social,
                                                    'address':all_address,
                                                    })

def enquery_form_submit(request):
    full_name = request.POST["enq_name"]
    mobile_no = request.POST["enq_email"] 
    email = request.POST["enq_phone"]
    subject = request.POST["enq_subject"]
    message = request.POST["enq_message"]
    enquery_info = Enquery(name=full_name, mobile=mobile_no, email=email, subject=subject, message=message)
    enquery_info.save()  
    # return JsonResponse({"success":True}, status=200)

    return redirect('index')