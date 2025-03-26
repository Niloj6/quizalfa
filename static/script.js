import { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

const questions = [
  { question: "O que significa 'QAP'?", options: ["Desligar", "Está na escuta?", "Qual endereço, local, posição"], answer: "Está na escuta?" },
  { question: "O que significa 'QSL'?", options: ["Está com interferência na comunicação?", "Entendido, acusado o recebimento da mensagem", "Qual nome do operador ou da estação"], answer: "Entendido, acusado o recebimento da mensagem" },
  { question: "O que significa 'QTH'?", options: ["Qual endereço, local, posição", "Devo parar de transmitir?", "Está preparado?"], answer: "Qual endereço, local, posição" },
  { question: "O que significa 'QRN'?", options: ["Está com interferência na comunicação?", "Está preparado?", "Você está ocupado?"], answer: "Está com interferência na comunicação?" },
  { question: "O que significa 'QRZ'?", options: ["Quem está me chamando?", "Qual distância da estação?", "Transmita mais devagar"], answer: "Quem está me chamando?" }
];

export default function QuizApp() {
  const [shuffledQuestions, setShuffledQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);

  useEffect(() => {
    setShuffledQuestions(questions.sort(() => Math.random() - 0.5));
  }, []);

  const handleAnswer = (option) => {
    if (option === shuffledQuestions[currentQuestion].answer) {
      setScore(score + 1);
    }

    const nextQuestion = currentQuestion + 1;
    if (nextQuestion < shuffledQuestions.length) {
      setCurrentQuestion(nextQuestion);
    } else {
      setShowScore(true);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <motion.div 
        className="w-full max-w-md"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Card className="p-6 shadow-lg rounded-2xl bg-white">
          {showScore ? (
            <CardContent className="text-center">
              <h2 className="text-2xl font-bold">Você acertou {score} de {shuffledQuestions.length} perguntas!</h2>
            </CardContent>
          ) : (
            <CardContent>
              <h2 className="text-xl font-bold mb-4">{shuffledQuestions[currentQuestion]?.question}</h2>
              <div className="space-y-2">
                {shuffledQuestions[currentQuestion]?.options.map((option, index) => (
                  <Button 
                    key={index} 
                    className="w-full" 
                    onClick={() => handleAnswer(option)}
                  >
                    {option}
                  </Button>
                ))}
              </div>
            </CardContent>
          )}
        </Card>
      </motion.div>
    </div>
  );
}