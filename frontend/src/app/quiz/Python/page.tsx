import axios from "axios";

const fetchQuestions = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/dummy-quiz/", {
      withCredentials: true, // If Django uses authentication
    });
    console.log("Data received:", response.data);
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error("Error fetching data:", error.response ? error.response.data : error.message);
    } else {
      console.error("Unknown Error fetching data:", error);
    }
  }
};

fetchQuestions();
export default function PythonQuizPage() {
  return (
    <div>
      <h1>Python Quiz</h1>
      <p>Welcome to the Python quiz page.</p>
    </div>
  );
}
