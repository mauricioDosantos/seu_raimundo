from django.urls import path
from .views import main, article


urlpatterns = [
    path('', main, name='blog'),
<<<<<<< HEAD
    path('article/<str:URLTitle>', article, name='article'),

=======
    path('article/<int:articleId>', article, name='article')
>>>>>>> origin
]
