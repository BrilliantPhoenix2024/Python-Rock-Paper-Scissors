import random

choices = ['r', 'p', 's']

choice_meaning = {
        'r':"Rock",
        'p':"Paper",
        's':"Scissors"
    }

user_score = 0
ai_score = 0

i = 0
    
while i < 5:
    user_choice = input("Select from Rock, Paper, Scissors (r, p, s): ")
    
    ai_choice = random.choice(choices)

    if user_choice in choices:
        print(f"Your choice is {choice_meaning[user_choice]} and AI choice is {choice_meaning[ai_choice]}.")
        # r > s - p > r - s > p
        if user_choice == ai_choice:
            print('Tie')
        elif ((user_choice == 'r') and (ai_choice == 's')) or ((user_choice == 'p') and (ai_choice == 'r')) or ((user_choice == 's') and (ai_choice == 'p')):
            print('You Won!')
            user_score += 1
        else:
            print("AI Won!")
            ai_score += 1
    else:
        print('Invalid input')
        i -= 1

    print(f'User Score:{user_score} | AI Score:{ai_score}')
    print('\n', '-'*15, '\n')
    
    i += 1

if user_score > ai_score:
    print(f"User Won with {user_score} scores.")
elif user_score < ai_score:
    print(f'AI won with {ai_score} Scores.')
else:
    print('You are Tie!')