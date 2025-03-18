"use client";

import { Button } from "@nextui-org/react";

export default function PythonQuizPage() {
  const startQuiz = () => {
    alert("Starting Python Quiz!");
  };

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
