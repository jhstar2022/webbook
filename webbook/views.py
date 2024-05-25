from django.shortcuts import render
from django.views import View


class index(View):
    def get(self,request):
        return render(request, 'webbook/index.html')

class base(View):
    def get(self,request):
        return render(request, 'webbook/base.html')