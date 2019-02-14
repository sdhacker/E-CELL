from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from blogs.models import blog
from gallery.models import gallery


class BlogHome(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHome, self).get_context_data(**kwargs)
        context['articles'] = blog.objects.all()
        context['snaps'] = gallery.objects.all().order_by('index')
        return context


class Blogdetails(DetailView):
    template_name = 'details.html'
    model = blog
