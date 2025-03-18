from backend.classes.questions import QuizQuestion
# Creating a list of QuizQuestion instances
quiz_questions = [
    QuizQuestion(
        id = 1,
        question_text="What is the output of `print(2 ** 3)`?",
        correct_answers=["8"],
        wrong_answers=["6", "9", "16"],
        explanation_correct="`2 ** 3` means 2 raised to the power 3, which equals 8.",
        explanation_wrong="Exponentiation in Python is done using `**`, not `*`."
    ),
    QuizQuestion(
        id = 2,
        question_text="Which of the following is a mutable data type in Python?",
        correct_answers=["List"],
        wrong_answers=["Tuple", "String", "Integer"],
        explanation_correct="Lists are mutable, meaning they can be changed after creation.",
        explanation_wrong="Tuples, strings, and integers are immutable in Python."
    ),
    QuizQuestion(
        id = 3,
        question_text="What will `len(['a', 'b', 'c', 'd'])` return?",
        correct_answers=["4"],
        wrong_answers=["3", "5", "Error"],
        explanation_correct="`len()` returns the number of elements in a list, which is 4.",
        explanation_wrong="It does not count from 0; it counts total elements."
    ),
    QuizQuestion(
        id = 4,
        question_text="How do you define a function in Python?",
        correct_answers=["Using `def` keyword"],
        wrong_answers=["Using `function` keyword", "Using `func` keyword", "Using `define` keyword"],
        explanation_correct="Python functions are defined using the `def` keyword.",
        explanation_wrong="There is no `function` or `define` keyword in Python."
    ),
    QuizQuestion(
        id = 5,
        question_text="What will be the output of `bool([])`?",
        correct_answers=["False"],
        wrong_answers=["True", "None", "Error"],
        explanation_correct="An empty list is considered `False` in Python.",
        explanation_wrong="Only non-empty lists are `True`."
    ),
]

# Print all questions
for question in quiz_questions:
    print(question, "\n")
