from instances.questions import quiz_questions
from django.http import JsonResponse
import pyrebase

# Firebase configuration
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
    return JsonResponse([{
        "id": question.id,
        "question_text": question.question_text,
        "correct_answers": question.correct_answers,
        "wrong_answers": question.wrong_answers,
        "explanation_correct": question.explanation_correct,
        "explanation_wrong": question.explanation_wrong
    } for question in quiz_questions], safe=False)


def push_dummy_quiz_data(request):
    dummy_quiz_data = {
        "quiz1": {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": "Paris"
        },
        "quiz2": {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        }
    }

    # Push data to Firebase
    firebase_db.child("quizzes").set(dummy_quiz_data)

    return JsonResponse({"message": "Dummy quiz data added to Firebase!"})