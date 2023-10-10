import random

class SLLA:
    def __init__(self):
        self.vocabulary = {
            "girl": "msichana",
            "boy": "mvulana",
            "food": "chakula",
            "fish": "samaki",
            "car": "gari",
            "cat": "paka",
            "dog": "mbwa",
            "phone": "simu",
            "sleep": "lala",
            "eat": "kula",
        }
    def get_random_question(self):
        word = random.choice(list(self.vocabulary.keys()))
        corect_answer = self.vocabulary[word]
        return word, corect_answer
    
    def conduct_quiz(self):
        score = 0
        num_questions = 3
        for _ in range(num_questions):
            word, corect_answer = self.get_random_question()
            user_answer = input(f"what is {word} in swahili?").strip()
            if user_answer.lower() == corect_answer.lower():
                print("corect")
                score += 1
            else:
                print(f"false! The corect answer is '{corect_answer}.")
        print(f"comple! score = {score}/{num_questions}")
        
if __name__ == "__main__":
    assistant = SLLA()
    assistant.conduct_quiz()                    
                
                
                
                
                
                
                
                
                