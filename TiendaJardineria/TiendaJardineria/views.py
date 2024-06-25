from django.views.generic import View
from django.shortcuts import render
class HomeView(View):
    def get(sefl, request, *args, **kwargs):
        context = {

        }
        return render(request, 'home.html', context)
   