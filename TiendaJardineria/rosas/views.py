from django.shortcuts import render
from django.views.generic import View 
# Create your views here.
class RosasListView(View):
    def get(self, request, *args, **kwargs):
        context = {
           
        }
        return render(request, 'rosalist.html', context)