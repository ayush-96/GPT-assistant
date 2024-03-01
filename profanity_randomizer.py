import random

profanity_list = ['Bitch', 'Asshole', 'Cunt',
                  'Dumbass', 'Twat']


def get_profanity():
    return profanity_list[random.randrange(0, len(profanity_list)-1)]
