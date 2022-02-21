from django.shortcuts import render
from .models import Post


def main(request):
    pub = Post.objects.order_by('-publiched_date')
    context = {'posts': pub}
    return render(request, 'index.html', context)
