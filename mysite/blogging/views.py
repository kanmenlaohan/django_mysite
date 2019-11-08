from django.shortcuts import render
from django.http import Http404
from blogging.models import Post


def list_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'list.html', context)


def detail_view(request, blog_id):
    try:
        post = Post.objects.get(pk=blog_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'posts': post}
    return render(request, 'detail.html', context)
