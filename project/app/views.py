from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.views.generic import TemplateView

# Create your views here.

class MainPage(TemplateView):
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        

        return context