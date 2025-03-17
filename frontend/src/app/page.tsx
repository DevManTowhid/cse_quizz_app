import { Button } from '@nextui-org/react';
import { useRouter } from 'next/navigation'
 
export default function Home() {
  const router = useRouter();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      {/* Hero Section */}
      <div className="text-center p-10">
        <h1 className="text-4xl font-bold text-gray-800">Test Your Knowledge</h1>
        <p className="mt-3 text-gray-600">Take quizzes on Python, Machine Learning, and Deep Learning!</p>
      </div>

      {/* Category Section */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 p-6">
        {['Python', 'Machine Learning', 'Deep Learning'].map((category) => (
          <Button  key={category} href={`/quiz/${category.toLowerCase()}`}>
            <div className="p-6 bg-white shadow-lg rounded-lg hover:bg-blue-500 hover:text-white cursor-pointer transition">
              <h2 className="text-2xl font-semibold text-center">{category}</h2>
            </div>
          </Button>
        ))}
      </div>
    </div>
  );
}
