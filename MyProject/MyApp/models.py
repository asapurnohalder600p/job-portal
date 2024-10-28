from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User_Model(AbstractUser):
    User_type=[('seeker','Seeker'),('recruiter','Recruiter')]

    user_type=models.CharField(max_length=10,null=True,choices=User_type)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    choiceskill=[
        ('python','PYTHON'),('java','JAVA'),('graphic','GRAPHIC'),('marketing','MERKETING'),
    ]
    Skill=models.CharField(choices=choiceskill,max_length=100,null=True)

class ViewerProfileModel(models.Model):

    user=models.ForeignKey(Custom_User_Model,on_delete=models.CASCADE,null=True,related_name='ViewerProfile')
    
    


class AdminProfileModel(models.Model):

    user=models.ForeignKey(Custom_User_Model,on_delete=models.CASCADE,null=True,related_name='AdminProfile')


class JobModel(models.Model):
    choiceskill=[
        ('python','PYTHON'),('java','JAVA'),('graphic','GRAPHIC'),('marketing','MERKETING'),
    ]
    choicescategory=[
        ('full_time',"Full Time"),
        ('part_time',"Part Time"),
    ]
    user=models.ForeignKey(Custom_User_Model,on_delete=models.CASCADE,null=True,related_name='jobmodel')
    job_title=models.CharField(max_length=100,null=True)
    Openings=models.CharField(max_length=100,null=True)
    Category=models.CharField(choices=choicescategory,max_length=100,null=True)
    Job_Dscriptions=models.TextField(null=True)
    Skill=models.CharField(choices=choiceskill,max_length=100,null=True)
    Job_Image=models.ImageField(upload_to='Media/job_img',null=True)
    
    
    def __str__(self):
        return f"{self.user.username}-{self.Skill}"
    
    
    
class jobApplyModel(models.Model):
    
    


    user=models.ForeignKey(Custom_User_Model,on_delete=models.CASCADE,null=True)
    job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True,)
    choiceskill=[
        ('python','PYTHON'),('java','JAVA'),('graphic','GRAPHIC'),('marketing','MERKETING'),
    ]
    Resume = models.FileField(upload_to="Media/Resume",max_length=200, null=True, blank=True) 
    Skill = models.CharField(max_length=200,choices=choiceskill, null=True) 
    Cover = models.TextField(null=True, blank=True) 

    
    def __str__(self) -> str:
        return self.user.username+"-"+self.job.job_title
    