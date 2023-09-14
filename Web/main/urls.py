from django.urls import path
from . import views

# cd web
# python manage.py runserver
urlpatterns = [
    path('', views.index),
    path('FAQs', views.FAQs),
    path('addfeedbacktodb', views.addfeedbacktodb, name='addfeedbacktodb'),
    path('gentext', views.gentext, name='gentext'),
]
