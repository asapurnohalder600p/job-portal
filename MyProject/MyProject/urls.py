
from django.contrib import admin
from django.urls import path
from MyProject.views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('HomePage/',homePage,name='homePage'),
    path('',loginPage,name='loginPage'),
    path('registerPage/',registerPage,name='registerPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('profilePage/',profilePage,name='profilePage'),
    path('profileEdit/',profileEdit,name='profileEdit'),

    path('addjob/',addjob,name='addjob'),
    path('joobFeed/',joobFeed,name='joobFeed'),
    path('createdjob/',createdjob,name='createdjob'),
    path('deletePage/ <int:id>/',deletePage,name='deletePage'),
    path('viewPage/ <int:id>/',viewPage,name='viewPage'),
    path('editpage/ <int:id>/',editpage,name='editpage'),
    
    
    path('applyjob/ <int:id>/',applyjob,name='applyjob'),
    path('applyedjob/',applyedjob,name='applyedjob'),
    
    
    path('searchJob/',searchJob,name='searchJob'),
    path('skillmachingPage/',skillmachingPage,name='skillmachingPage'),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
