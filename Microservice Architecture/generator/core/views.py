import random
from django.http import JsonResponse
from django.views import View


class NumberView(View):
    def get(self, *args, **kwargs):

        return JsonResponse({"number": random.randint(1, 1000)})
