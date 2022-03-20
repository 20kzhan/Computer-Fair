import random

def format_response(user_input):
    user_input = user_input.lower()

    if user_input in ("r", "rock", "1"):
        return "rock"
    elif user_input in ("p", "paper", "2"):
        return "paper"
    elif user_input in ("s", "scissors", "3"):
        return "scissors"
    print("Invalid Object!\n")
    return False

def play_game():
    while True:
        args = input("Pick one: Rock, Paper, Scissors: ")

        msg = format_response(args)
        if msg:
            break

    responses = ['rock',
                 'paper',
                 'scissors']

    random_res = random.choice(responses)
    results = {'rock': {'paper': f'CPU wins! It chose {random_res}.',
                        'scissors': f'You win! CPU chose {random_res}.'},
               'paper': {'rock': f'You win! CPU chose {random_res}.',
                         'scissors': f'CPU wins! It chose {random_res}.'},
               'scissors': {'rock': f'CPU wins! It chose {random_res}.',
                            'paper': f'You win! CPU chose {random_res}.'}}

    if random_res == f'{msg}':
        print(f"It's a Draw! I chose {random_res}.")
        print()
        return
    else:
        print(results[msg][random_res])
        print()
        return


if __name__ == '__main__':
    rps()