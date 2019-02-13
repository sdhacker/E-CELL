from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from blogs.models import blog


class BlogHome(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHome, self).get_context_data(**kwargs)
        context['articles'] = blog.objects.all()
        return context


class Blogdetails(DetailView):
    template_name = 'details.html'
    model = blog
