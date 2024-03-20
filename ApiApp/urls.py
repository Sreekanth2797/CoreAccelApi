from django.urls import path

from . import views

from .views import FileUploadView


urlpatterns = [
    path('', views.SampleHome, name = "Api-Home"),
    path('api/upload/', FileUploadView.as_view(), name='file-upload'),
]