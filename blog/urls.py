from django.urls import path
from .views import main, article


urlpatterns = [
    path('', main, name='blog'),
    path('article/<str:URLTitle>', article, name='article'),

]
