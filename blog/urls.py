from django.urls import path
from .views import main, one_post


urlpatterns = [
    path('', main, name='blog'),
    path('<post_id>', one_post, name='one_post')
]
