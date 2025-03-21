from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from google.cloud import firestore  
from instances.questions import quiz_questions  
from firebase_config import firestore_db as db  

# Debugging: Check Firestore connection
print("📌 Starting script: Connecting to Firestore...")

try:
    test_doc = db.collection("test").document("connection_test").get()
    if test_doc.exists:
        print("✅ Firestore is connected successfully!")
    else:
        print("⚠️ Firestore is connected, but test document does not exist.")
except Exception as e:
    print(f"❌ Firestore connection failed: {e}")

def get_dummy_questions(request):
    """Return a list of dummy quiz questions."""
    print("📌 get_dummy_questions() called!")

    try:
        questions_list = [
            {
                "id": question.id,
                "question_text": question.question_text,
                "correct_answers": question.correct_answers,
                "wrong_answers": question.wrong_answers,
                "explanation_correct": question.explanation_correct,
                "explanation_wrong": question.explanation_wrong
            }
            for question in quiz_questions
        ]
        print(f"✅ Retrieved {len(questions_list)} questions successfully!")
        return JsonResponse(questions_list, safe=False)

    except Exception as e:
        print(f"❌ Error retrieving questions: {e}")
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def push_dummy_quiz_data(request):
    """Push dummy quiz data to Firestore."""
    print("📌 push_dummy_quiz_data() called!")

    if request.method != "POST":
        print("❌ Invalid request method. Expected POST.")
        return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)

    try:
        print("🚀 Pushing quiz data to Firestore...")
        
        for question in quiz_questions:
            print(f"📝 Pushing question ID: {question.id}")

            # Firestore write operation
            db.collection("quizzes").document(str(question.id)).set({
                "id": question.id,
                "question_text": question.question_text,
                "correct_answers": question.correct_answers,
                "wrong_answers": question.wrong_answers,
                "explanation_correct": question.explanation_correct,
                "explanation_wrong": question.explanation_wrong
            })

        print("✅ All dummy quiz data added to Firestore!")
        return JsonResponse({"message": "Dummy quiz data added to Firestore!"})

    except Exception as e:
        print(f"❌ Firestore error: {e}")
        return JsonResponse({"error": str(e)}, status=500)
