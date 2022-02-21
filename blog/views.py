from django.shortcuts import render
from .models import Post


# template body: https://blog01.superservidor.info/
# https://blog.wedologos.com.br/exemplos-de-blogs/
def main(request):
    pub = Post.objects.order_by('-publiched_date')
    context = {'posts': pub}
    return render(request, 'index.html', context)
