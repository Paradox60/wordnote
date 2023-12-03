#from datetime import datetime
#import datetime as date
#from wordnote.SqLt.db_base import *
#from wordnote.wins.library import *
#from random import randint
import random

def testing_list(self, cards):
    list = []
    random_numbers = []
    id_card = []
    word_list = []
    print(len(cards))
    clean_cards = []
    for card in cards:
        if card.progress < 100:
            clean_cards.append(card)
    print(len(clean_cards))
    #if len(clean_cards) < 4:
        #self.delete_handler(8)
    if len(clean_cards) < 20 and len(clean_cards) >= 4:
        random_numbers = random.sample(range(-1, len(clean_cards)), len(clean_cards))
    else:
        random_numbers = random.sample(range(-1, len(clean_cards)), 20)

    for word in random_numbers:
        id_card.append(clean_cards[word].card_id)
        word_list.append(clean_cards[word].word)
    list.append(id_card)
    list.append(word_list)
    print(list)


    return list


