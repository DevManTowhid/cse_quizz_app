interface Question {
    question: string;
    answers: string[];
}

export default function QuestionCard({ question, index, totalQuestions, handleAnswer }: { question: Question; index: number; totalQuestions: number; handleAnswer: (answer: string) => void }) {
    return (
        <div className="bg-white p-6 shadow-lg rounded-lg">
            <h2 className="text-xl font-semibold">{question.question}</h2>
            <div className="grid grid-cols-1 gap-4 mt-4">
                {question.answers.map((answer, i) => (
                    <button
                        key={i}
                        onClick={() => handleAnswer(answer)}
                        className="p-4 bg-gray-100 shadow-md rounded-lg hover:bg-blue-500 hover:text-white cursor-pointer transition"
                    >
                        {answer}
                    </button>
                ))}
            </div>
            <div className="mt-4">
                <p>
                    Question {index + 1} of {totalQuestions}
                </p>
            </div>
        </div>
    );
}
