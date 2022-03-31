from django.urls import path
from .views import main, article


urlpatterns = [
    path('', main, name='blog'),
    path('article/<int:articleId>', article, name='article')
]
