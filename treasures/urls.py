from django.urls import path

from treasures.views import treasureform_view

urlpatterns = [
    path('', treasureform_view)
]
