"use client";
import axios from "axios";
import { useEffect, useState } from "react";

// Define the expected structure of a quiz question
interface QuizQuestion {
  id: number;
  question_text: string;
  correct_answers: string[];
  wrong_answers: string[];
  explanation_correct: string;
  explanation_wrong: string;
}


const PythonQuizPage = () => {
  const [questions, setQuestions] = useState<QuizQuestion[]>([]);

  const fetchQuestions = async () => {
    try {
      const response = await axios.get("http://localhost:8000/dummy-quiz/", {
        withCredentials: true, // Keep this if Django uses authentication
      });
      console.log("Data received:", response.data);
      setQuestions(response.data); // Store data in state
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.error("Error fetching data:", error.message);
        console.error("Response:", error.response?.data); // Log response
      } else {
        console.error("Unknown Error fetching data:", error);
      }
    }
  };

  useEffect(() => {
    fetchQuestions();
  }, []);

  return (
    <div>
      <h1>Python Quiz</h1>
      {questions.length > 0 ? (
        questions.map((q, index) => <p key={index}>{q.question}</p>)
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default PythonQuizPage;
