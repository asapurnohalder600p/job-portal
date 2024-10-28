from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from MyApp.models import *
from django.contrib.auth.decorators import login_required

from django.db.models import Q


#loginPage 
def loginPage(req):
    if req.method=="POST":
        user=authenticate(username=req.POST.get('username'),password=req.POST.get('password'))
        if user:
            login(req,user)
            return redirect('homePage')
        
        else:
            return HttpResponse(req,"You have don't account")


    return render(req,'loginPage.html')


#registerPage
def registerPage(req):
    if req.method=="POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        c_password=req.POST.get('c_password')
        email=req.POST.get('email')
        user_type=req.POST.get('user_type')

        if password==c_password:
            user=Custom_User_Model.objects.create_user(username=username,user_type=user_type,email=email,password=password)

            if user_type == "seeker":
                ViewerProfileModel.objects.create(user=user)

            
            elif user_type == "recruiter":
                AdminProfileModel.objects.create(user=user)

            return redirect('loginPage')

    
    return render(req,'registerPage.html')


def logoutPage(req):
    logout(req)
    return redirect('loginPage')

#homePage
@login_required
def homePage(req):


    
    return render(req,'homePage.html')


#profilePage
@login_required
def profilePage(req):

    return render(req,'profilePage.html')


@login_required
def profileEdit(req):
    user=req.user
    if req.method=="POST":
        
        user.username=req.POST.get('username')
        user.email=req.POST.get('email')
        user.first_name=req.POST.get('first_name')
        user.last_name=req.POST.get('last_name')
        user.Profile_Pic=req.FILES.get('Profile_Pic')
        user.save()
        
        return redirect('profilePage')
    
    
    return render(req,'profileEdit.html')
#Add form
@login_required
def addjob(req):
    user=req.user
    if req.method == 'POST':
        job=JobModel.objects.create(
            user=user,
            job_title=req.POST.get('job_title'),
            Openings=req.POST.get('Openings'),
            Category=req.POST.get('Category'),
            Job_Dscriptions=req.POST.get('Job_Dscriptions'),
            Skill=req.POST.get('Skill'),
            Job_Image=req.FILES.get('Job_Image'),
        )
        return redirect('createdjob')
        
    
    return render(req,'addjob.html')

@login_required
def joobFeed(req):
   
    jobs=JobModel.objects.all()
    
    context={
        'jobs':jobs,
    }
    
    return render(req,'joobFeed.html',context)


@login_required
def createdjob(req):
    user=req.user
    jobs=JobModel.objects.filter(user=user)
    
    context={
        'jobs':jobs,
    }
    
    return render(req,'createdjob.html',context)


@login_required
def deletePage(req,id):
    JobModel.objects.filter(id=id).delete()
    return redirect('createdjob')
    
    
@login_required
def viewPage(req,id):
    user=req.user
    jobs=JobModel.objects.filter(id=id)
    
    context={
        'jobs':jobs,
    }
    
    return render(req,'viewPage.html',context)
@login_required
def editpage(req,id):
    user=req.user
   
    if req.method == 'POST':
        
        job_id=req.POST.get('job_id')
        
        job=JobModel(
            id=job_id,
            user=user,
            job_title=req.POST.get('job_title'),
            Openings=req.POST.get('Openings'),
            Category=req.POST.get('Category'),
            Job_Dscriptions=req.POST.get('Job_Dscriptions'),
            Skill=req.POST.get('Skill'),
            Job_Image=req.FILES.get('Job_Image'),
        )
        job.save()
        return redirect('createdjob')
        
    jobs=JobModel.objects.get(id=id)
    
    context={
        'job':jobs,
    }
    
    return render(req,'editpage.html',context)



@login_required
def applyjob(req,id):
    user=req.user
    job=JobModel.objects.get(id=id)
    if req.method == 'POST':
        applyed=jobApplyModel.objects.create(
            
                user=user,
                job=job,
                Resume=req.FILES.get('Resume'),
                Skill=req.POST.get('Skill'),
                Cover=req.POST.get('Cover'),
            )
        
        return redirect('applyedjob')
        
    
    context={
        'job':job
    }
    
    return render(req,'applyjob.html',context)

def applyedjob(req):
    user=req.user
    job=jobApplyModel.objects.filter(user=user)
    context={
        'job':job
    }
    return render(req,'applyedjob.html',context)



def searchJob(request):
    
    query = request.GET.get('query')
    
    if query:
        
        jobs = JobModel.objects.filter(Q(job_title__icontains=query) 
                                       |Q(Skill__icontains=query) 
                                       |Q(Category__icontains=query))
    
    else:
        jobs = JobModel.objects.none()
        
    context={
        'jobs':jobs,
        'query':query
    }
    
    return render(request,"searchJob.html",context)


@login_required
def skillmachingPage(req):
    
    user=req.user
    if user.user_type=='seeker':
        my_skill=user.Skill
        jobs=JobModel.objects.filter(Skill=my_skill)
        context={
            'jobs':jobs,
        }
        
    return render(req,'skillmachingPage.html',context)
