import random

class MathQuiz:
    def __init__(self):
        self.num1 = random.randint(1, 20)
        self.num2 = random.randint(1, 20)
        self.operator = random.choice(['+', '-'])

    def generate_question(self):
        if self.operator == '+':
            question = f"What is {self.num1} + {self.num2}?"
        else:
            question = f"What is {self.num1} - {self.num2}?"
        return question

    def check_answer(self, user_answer):
        if self.operator == '+':
            correct_answer = self.num1 + self.num2
        else:
            correct_answer = self.num1 - self.num2
        
        if user_answer == correct_answer:
            return True
        else:
            return False

# Main function to run the program
def main():
    print("Welcome to Math Quiz!")
    print("You will be asked simple addition or subtraction questions.")
    print("Please enter your answers as integers.")
    print("Let's begin!")

    # Ask 5 questions
    num_questions = 5
    correct_answers = 0
    quiz = MathQuiz()
    
    for _ in range(num_questions):
        question = quiz.generate_question()
        print(question)
        user_answer = int(input("Your answer: "))
        if quiz.check_answer(user_answer):
            print("Correct!\n")
            correct_answers += 1
        else:
            print("Incorrect.\n")

    # Display final score
    print(f"Quiz completed! You got {correct_answers} out of {num_questions} questions correct.")

# Run the main function
if __name__ == "__main__":
    main()
