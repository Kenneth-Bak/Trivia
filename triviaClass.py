import random # import random module
# open questions file and assign to list
with open('questions.txt', 'r') as q:
    # assign constant QUESTIONS list
    QUESTIONS = [line.strip() for line in q]
# open answer file and assign to list
with open('answer.txt', 'r') as a:
    # assign constant ANSWER and ANSWER_LIST lists
    ANSWER = [line.strip() for line in a]
    ANSWER_LIST = [t.strip().split(',')
                   for t in ANSWER if len(t) > 0]

class Trivia: # define Trivia class
    # define initializer
    def __init__(self):
        # class attributes
        self.__question = ''
        self.__answer1 = ''
        self.__answer2 = ''
        self.__answer3 = ''
        self.__answer4 = ''
        self.__correct = ''
        self.__count1 = []
        self.__count2 = 0

    def set_question(self): # define method
        # assign random number
        number = random.randrange(0, 9)
        # while the random number has been used try another
        while number in self.__count1:
            number = random.randrange(0, 9)
        self.__count1.append(number) # append the random number to list
        self.__question = QUESTIONS[number] # assign question to attribute
        print(self.__question) # print question
        # loop through ANSWER_LIST
        for i in ANSWER_LIST:
            if i == ANSWER_LIST[number]: # answer corresponding to question
                # assign possible answers and correct answer to attributes
                self.__answer1 = i[0]
                self.__answer2 = i[1]
                self.__answer3 = i[2]
                self.__answer4 = i[3]
                self.__correct = i[4]

    def get_answer(self): # define method
        # print possible answers
        print(self.__answer1, '\n', self.__answer2, '\n',
              self.__answer3, '\n', self.__answer4, sep='')

    def set_answer(self, answer): # define method
        # checks if correct or wrong, prints accordingly
        if answer == self.__correct:
            print('Correct!')
            self.__count2 += 1 # add 1 to counter attribute
        else:
            print('Wrong!')

    def show(self): # define method
        # return counter of correct answers
        return self.__count2

    def clear(self): # define method
        # clear all attributes
        self.__question = ''
        self.__answer1 = ''
        self.__answer2 = ''
        self.__answer3 = ''
        self.__answer4 = ''
        self.__correct = ''
        self.__count1 = []
        self.__count2 = 0
