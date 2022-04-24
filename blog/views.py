from django.shortcuts import render
from .models import Post, Attachment, Contact
import ipdb


# template body: https://blog01.superservidor.info/
# https://blog.wedologos.com.br/exemplos-de-blogs/
def description_replace():
    return



def main(request):
    pub = Post.objects.filter(active=True).order_by('-publiched_date')
    first_pub = Post.objects.order_by('-publiched_date').first()
    all_pub = pub.exclude(id=first_pub.id)

    #ipdb.set_trace()
    atts = Attachment.objects.order_by('-id')[:10]

    contacts = Contact.objects.all()

    context = {
        'posts': pub,
        'first_pub': first_pub,
        'attachments': atts,
        'contacts': contacts
    }

    return render(request, 'index.html', context)

<<<<<<< HEAD
def article(request, URLTitle):
    #ipdb.set_trace()
    URLT = URLTitle.replace('-',' ')
=======
def article(request, articleId):
    #ipdb.set_trace()
>>>>>>> origin
    pub = Post.objects.filter(active=True).order_by('-publiched_date')
    first_pub = Post.objects.order_by('-publiched_date').first()
    all_pub = pub.exclude(id=first_pub.id)
    atts = Attachment.objects.order_by('-id')[:10]
<<<<<<< HEAD
    article = Post.objects.get(title=URLT) #get object or 404
    contacts = Contact.objects.all()

    context = {
=======
    article = Post.objects.get(id=articleId) #get object or 404
    contacts = Contact.objects.all()


    context = {
        'id': articleId,
>>>>>>> origin
        'article': article,
        'posts': all_pub,
        'first_pub': first_pub,
        'attachments': atts,
        'contacts': contacts
    }
    return render(request, 'article.html', context)
