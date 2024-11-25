from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


# Create your views here.


class MainPage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context.update(
                {
                    'username': self.request.user.username,
                    'email': self.request.user.email,
                    'first_name': self.request.user.first_name,
                    'last_name': self.request.user.last_name,
                }
            )

        context.update(
            {
                "title": "Главная страница",
            }
        )

        return context


class CustomLoginView(LoginView):
    template_name = 'login.html'