from django.contrib import admin
from django.urls import path

from .views import person_list, person_new, persons_update, persons_delete

urlpatterns = [
    path('list/', person_list, name="person_list"),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
]
