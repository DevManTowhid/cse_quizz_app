from instances.questions import quiz_questions
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyrebase
import json

# Firebase configuration (Move to environment variables in production)
firebase_config = {
    "apiKey": "your_api_key",
    "authDomain": "your_auth_domain",
    "databaseURL": "your_database_url",
    "storageBucket": "your_storage_bucket"
}

firebase = pyrebase.initialize_app(firebase_config)
firebase_db = firebase.database()

def getdummyquestions(request):
    """Return a list of dummy quiz questions."""
    return JsonResponse([
        {
            "id": question.id,
            "question_text": question.question_text,
            "correct_answers": question.correct_answers,
            "wrong_answers": question.wrong_answers,
            "explanation_correct": question.explanation_correct,
            "explanation_wrong": question.explanation_wrong
        }
        for question in quiz_questions
    ], safe=False)


@csrf_exempt  # Needed if sending requests from frontend without CSRF token
def push_dummy_quiz_data(request):
    """Push dummy quiz data to Firebase."""

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

    try:
        # Convert quiz_questions to dictionary format
        quiz_data = {
            f"question_{i+1}": {
                "id": question.id,
                "question_text": question.question_text,
                "correct_answers": question.correct_answers,
                "wrong_answers": question.wrong_answers,
                "explanation_correct": question.explanation_correct,
                "explanation_wrong": question.explanation_wrong
            }
            for i, question in enumerate(quiz_questions)
        }

        # Push data to Firebase
        firebase_db.child("quizzes").set(quiz_data)

        return JsonResponse({"message": "Dummy quiz data added to Firebase!"})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
