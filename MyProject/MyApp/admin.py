from django.contrib import admin
from MyApp.models import *

# Register your models here.
admin.site.register(Custom_User_Model)
admin.site.register(ViewerProfileModel)
admin.site.register(AdminProfileModel) 
admin.site.register(JobModel) 
admin.site.register(jobApplyModel) 