from django.contrib import admin
from django.urls import path
from .views import getdummyquestions  # Import your view

urlpatterns = [
    path("admin/", admin.site.urls),  # Ensure Django admin is accessible
    path("dummy-quiz/", getdummyquestions, name="dummy-quiz"),
]
