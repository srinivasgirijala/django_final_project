from django.urls import path
from.import views
urlpatterns=[
    path('dashboard/',views.dashboard,name='dashboard'),
    path('About/',views.About,name='About'),
    path('careers/',views.careers,name='careers'),
    path('contact/',views.contact,name='contact'),
    path('become/',views.become,name='become'),
    path('created/',views.created,name='created'),
    path('technologies/',views.technologies,name='technologies'),
    path('training/',views.training,name='training'),
]