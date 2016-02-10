from trivia import Trivia # import Trivia class

def main():

    user1 = play() # call play function
    user2 = play()
    # condition checks the winner
    if user1[0] == user2[0]:
        print('It it a tie!')
    elif user1[0] > user2[0]:
        print(user1[1], 'wins with', user1[0], 'correct answers to', user2[0])
    else:
        print(user2[1], 'wins with', user2[0], 'correct answers to', user1[0])

def play():
    # the play function, input your name
    name = input('Enter your name: ')
    player = Trivia() # call Trivia class
    print(name, 'answer these 5 questions:')
    for i in range(5): # loop for 5 questions
        player.set_question()
        player.get_answer()
        player.set_answer(input('Your answer: '))
        print()
    print('Correct answers: ', player.show()) # print number of correct answer
    print()
    correct = player.show() # assign correct answers to correct
    player.clear() # clear player data
    return correct, name # return the number of correct answers and the name

main() # call main
