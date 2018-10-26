import datetime
import random

from Questions import Add, Multiply

class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # generate 10 random questions with numbers from 1 to 10
        # add these questions into self.questions

        question_types = (Add, Multiply)
        
        for _ in range(10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            question = random.choice(question_types)
            self.questions.append(question(num1, num2))
        
    def take_quiz(self):
        # log the start time
        # ask all of the questions
        # log if they got the question right
        # log the end time
        # show a summary
        self.start_time = datetime.datetime.now()

        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()

        return self.summary()
        
    def total_correct(self):
        #create this method
        total = 0

        for answer in self.answers:
            if answer[0]:
                total += 1
        
        return total

    def summary(self):
        # print how many you got right and the total # of questions. 5/10
        # print the total time for the quiz: 30 seconds!
        print("\nYou got {} out of {} right!".format(
            self.total_correct(), len(self.questions)
        ))

        print("It took you {} seconds total.".format(
            (self.end_time - self.start_time).seconds
        ))
    
    def ask(self, questions):
        correct = False
        question_start = datetime.datetime.now()
        answer = input(questions.text + ' : ')
        #print('{}--{}'.format(type(answer), type(questions.answer)))
        if answer == questions.answer:
            correct = True

        question_end = datetime.datetime.now()
        
        return correct, question_end - question_start

Quiz().take_quiz()