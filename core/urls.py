from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    #Front Page
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
    path('explore/<int:eid>/', views.explorespecific, name='explorespecific'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:eid>/', views.blogspecific, name='blogspecific'),

    path('database/', views.database, name='db'),
    path('map/', views.plasticmap, name='plasticmap'),
    path('map/mcps/', views.plasticmapmcps, name='plasticmapmcps'),
    path('getField/<int:eid>/<str:name>/<int:index>/', views.getfield, name='getfield'),
    path('getField/mcps/<int:eid>/<str:name>/<int:index>/', views.getfieldmcps, name='getfieldmcps'),



##    #Course Signups and Stuff
##    path('course/<str:cid>/', views.loadCourse, name='coursePage'),
##    path('course/<str:cid>/join/', views.joinCourse, name='joinCourse'),
##    path('course/private/join/', views.joinCoursePrivate, name='joinCoursePrivate'),
##    path('courseList/', views.courseList, name="courseList"),
##    path('courseView/', views.courseView, name="courseView"),
##    path('leaveCourse/<str:cid>/', views.leaveCourse, name="courseLeave"),
##
##    #Account Management
##    path('register/', views.register, name="register"),
##    path('login/', views.loginu, name="login"),
##    path('logout/', views.logoutu, name="logout"),
##    #path('manage/', views.manageAccount, name="manageAccount"),
    
]
