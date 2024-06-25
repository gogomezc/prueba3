from django.urls import path
from .views import RosasListView

app_name="rosas"

urlpatterns = [
    path('', RosasListView.as_view(), name="home"),
]