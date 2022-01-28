import requests
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        return {
            'number': requests.get('http://127.0.0.1:8081/').json()
        }
