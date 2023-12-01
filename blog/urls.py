from django.urls import path

from .views import BlogListView, AboutPageView, ImputPageView, StatPageView, GrayPageView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('imput/', ImputPageView.as_view(), name='imput'),
    path('stat/', StatPageView.as_view(), name='stat'),
    path('gray/', GrayPageView.as_view(), name='gray')

]