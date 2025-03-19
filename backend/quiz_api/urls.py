from django.contrib import admin
from django.urls import path
from .views import getdummyquestions, push_dummy_quiz_data  # Import your views

urlpatterns = [
    path("admin/", admin.site.urls),  # Ensure Django admin is accessible
    path("dummy-quiz/", getdummyquestions, name="dummy-quiz"),
    path('push-quiz-data/', push_dummy_quiz_data, name='push-quiz-data')
]
