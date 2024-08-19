from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('faqs/', FaqsView.as_view(), name='faqs'),
    path('busines/', BusinesView.as_view(), name='busines'),
    # path('comment/', CommentView.as_view(), name='comment'),
    path('client/', ClientView.as_view(), name='client'),
    path('users/', UsersView.as_view(), name='users'),

]

