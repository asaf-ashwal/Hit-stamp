import random


def is_it_right(game,num):
    result = game['secret_name'][len(game['display_num'])] == num
    if result:
        print('good guess')
        game['display_num'].append(num)
        game['wrong_guesses'] = []
    else:
        game['wrong_guesses'].append(num)
        print('sorry try again')
        game['trys'] += 1
        
        
        
def random_num():
    return list(str(random.randint(1000,1999)))

def user_choice(display_num,wrong_list):
    while True:
        print(f'your last guesses {wrong_list}')
        if len(display_num) > 0:
            print('your correct guesses: ',display_num)
        user_num = input('Enter a number between 0 and 9 inclusive: ')
        if user_num.isdigit() and len(user_num) == 1 and user_num not in wrong_list:
            return user_num
        print('Non standard tax')
    


def init_game():
    game = {
        'secret_name' :random_num(),
        'display_num':[],
        'trys':0,
        'wrong_guesses':[]
    }
    while True:
        print('secret num: ',game['secret_name'])
        user_num = user_choice(game['display_num'],game['wrong_guesses'])
        result = is_it_right(game,user_num)
        if game['display_num'] == game['secret_name']:
            print('!!!  you won  !!!')
            break
        if game['trys'] == 3:
            print('!!!  you lost  !!!')
            break            
        