from django.urls import path
from blogging.views import list_view, detail_view, stub_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('blogging', stub_view, name="stub_view"),
    path('blog/<int:post_id>/', detail_view, name="blog_detail"),
]
