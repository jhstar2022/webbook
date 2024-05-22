from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class index(View):
    def get(self, request):
        return render(request, 'webbook/index.html')