from django.views.generic import ListView

# Create your views here.


class BlogListView(ListView):
    template_name = "blogs/blog_list.html"


blog_list = BlogListView.as_view()
