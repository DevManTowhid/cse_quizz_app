class QuizQuestion:
    def __init__(self, id, question_text, correct_answers, wrong_answers, explanation_correct, explanation_wrong):
        self.id = id
        self.question_text = question_text
        self.correct_answers = correct_answers  # List of correct answers
        self.wrong_answers = wrong_answers  # List of wrong answers
        self.explanation_correct = explanation_correct
        self.explanation_wrong = explanation_wrong

    def is_correct(self, answer):
        """Check if an answer is correct."""
        return answer in self.correct_answers

    def __str__(self):
        return f"Question: {self.question_text}\nCorrect: {self.correct_answers}\nWrong: {self.wrong_answers}"
