from django.shortcuts import render
from .models import Post, Attachment, Contact
import ipdb


# template body: https://blog01.superservidor.info/
# https://blog.wedologos.com.br/exemplos-de-blogs/
def description_replace():
    return


def main(request):
    pub = Post.objects.filter(active=True).order_by('-publiched_date')
    first_pub = Post.objects.filter(
        active=True
    ).order_by('-publiched_date').first()

    if not first_pub:
        return render(request, 'no_pubs.html')

    all_pub = pub.exclude(id=first_pub.id)
    atts = Attachment.objects.order_by('-id')[:10]
    contacts = Contact.objects.all()

    context = {
        'posts': all_pub,
        'first_pub': first_pub,
        'attachments': atts,
        'contacts': contacts
    }

    return render(request, 'index.html', context)
