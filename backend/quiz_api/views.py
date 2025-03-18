from instances.questions import quiz_questions
from django.http import JsonResponse
def getdummyquestions(request):
    """Return a list of dummy quiz questions."""
    return JsonResponse([{
        "id": question.id,
        "question_text": question.question_text,
        "correct_answers": question.correct_answers,
        "wrong_answers": question.wrong_answers,
        "explanation_correct": question.explanation_correct,
        "explanation_wrong": question.explanation_wrong
    } for question in quiz_questions], safe=False)
# Compare this snippet from backend/quiz_api/urls.py:
# from django.urls import path
# from . import views
#

# urlpatterns = [
#     path('questions/', views.getdummyquestions),
# ]
# Compare this snippet from backend/quiz_api/views.py:        