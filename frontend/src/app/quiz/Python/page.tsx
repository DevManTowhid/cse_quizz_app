"use client";
import quiz_questions from "backend/instances/quiz_questions.py";
import { Button } from "@nextui-org/react";

export default function PythonQuizPage() {
  const startQuiz = () => {
    alert("Starting Python Quiz!");
  };
const quiz_questions = [
  { question: "What is Python?", options: ["A snake", "A programming language", "A car"], answer: "A programming language" },
  { question: "Who created Python?", options: ["Guido van Rossum", "Elon Musk", "Bill Gates"], answer: "Guido van Rossum" },
];
const questions = [...quiz_questions];
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <h1 className="text-4xl font-bold text-gray-800">Python Quiz</h1>
      <p className="text-gray-600 mt-3">Test your Python knowledge with our quiz.</p>

      <Button
        color="primary"
        variant="solid"
        size="lg"
        className="mt-6"
        onClick={startQuiz}
      >
        Start Quiz
      </Button>
    </div>
  );
}
