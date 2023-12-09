from django.views.generic import ListView, TemplateView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class PostListView(ListView):
    paginate_by = 5


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ImputPageView(TemplateView):
    template_name = 'imput.html'


class StatPageView(TemplateView):
    template_name = 'stat.html'


class GrayPageView(TemplateView):
    template_name = 'gray.html'
