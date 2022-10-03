import random


class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):

        if self.rank in 'TJQK':
            return 10
        else:
            return 'A23456789'.index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return '%s%s' % (self.rank, self.suit)


class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == 'A':
                aces += 1
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = 'Карты %s:\n' % self.name
        for card in self.cards:
            text += str(card) + ' '
        text += '\nСумма карт: ' + str(self.get_value())
        return text


class Deck(object):
    def __init__(self):
        ranks = '23456789TJQKA'
        suits = 'БТЧП'
        self.cards = [Card(r, s) for r in ranks for s in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


def new_game():

    d = Deck()
    player_hand = Hand(name)
    dealer_hand = Hand('Дилер')
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print('=' * 20)
    print(player_hand)
    in_game = True

    while player_hand.get_value() < 21:
        ans = input('Взять карту или стоп? (h/s): ')
        if ans == 'h':
            player_hand.add_card(d.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:
                print('Ты проиграл!')
                in_game = False
        else:
            print('Вы пасанули!')
            break
    print('=' * 20)
    if in_game:

        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:
                print('У Дилера перебор')
                in_game = False
    if in_game:

        if player_hand.get_value() > dealer_hand.get_value():
            print('{} - победил!'.format(player_hand))
        elif player_hand.get_value() == dealer_hand.get_value():
            print('Ничья!')
        else:
            print('Дилер победил!')


print('=' * 20, '\nA - Туз\nK - Король\nQ - Дама\nJ - Валет\nT - Десять\n'
      '23456789 - Младшие карты\nМасти карт: Б - бубы, Т - трефы, Ч - черви, П - пики\n',
      '=' * 20, '\n')

name = input('Введите имя: ')
Hand(name)

new_game()
