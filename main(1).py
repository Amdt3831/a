# import matplotlib.pyplot as plt
# import pandas as pd


class Card:
    def __init__(self, damage):
        self.damage = damage


class Player:
    def __init__(self, name, score, health):
        self.score = score
        self.health = health
        self.name = name


class Card_a(Card):
    name = 'A'

    def __init__(self, damage):
        super().__init__(damage)


class Card_b(Card):
    name = 'B'
    pass


class Card_c(Card):
    name = 'C'
    pass


players = input().split(' ')

try:
    healths = list(map(int, input().split(' ')))
    damages = list(map(int, input().split(' ')))
except ValueError:
    print('\n')
    print('Invalid Command.')
    exit()
card_a = Card_a(damages[0])
card_b = Card_b(damages[1])
card_c = Card_c(damages[2])
round1 = input().split(' ')
round2 = input().split(' ')
round3 = input().split(' ')
player1 = Player(players[0], 0, healths[0])
player2 = Player(players[1], 0, healths[1])



def game(roundd):
    if roundd[0] == card_a.name:
        if roundd[1] == card_b.name and card_a.damage > card_b.damage:
            player1.score += 1
            player1.health -= card_b.damage
            player2.health -= card_a.damage
        elif roundd[1] == card_c.name and card_a.damage > card_c.damage:
            player1.score += 1
            player1.health -= card_c.damage
            player2.health -= card_a.damage
        elif roundd[1] == card_b.name and card_a.damage < card_b.damage:
            player2.score += 1
            player2.health -= card_a.damage
            player1.health -= card_b.damage
        elif roundd[1] == card_c.name and card_a.damage < card_c.damage:
            player2.score += 1
            player2.health -= card_a.damage
            player1.health -= card_c.damage
    elif roundd[0] == card_b.name:
        if roundd[1] == card_a.name and card_b.damage > card_a.damage:
            player1.score += 1
            player1.health -= card_a.damage
            player2.health -= card_b.damage
        elif roundd[1] == card_c.name and card_b.damage > card_c.damage:
            player1.score += 1
            player1.health -= card_c.damage
            player2.health -= card_b.damage
        elif roundd[1] == card_a.name and card_a.damage > card_b.damage:
            player2.score += 1
            player2.health -= card_b.damage
            player1.health -= card_a.damage
        elif roundd[1] == card_c.name and card_b.damage < card_c.damage:
            player2.score += 1
            player2.health -= card_b.damage
            player1.health -= card_c.damage
    elif roundd[0] == card_c.name:
        if roundd[1] == card_a.name and card_c.damage > card_a.damage:
            player1.score += 1
            player1.health -= card_a.damage
            player2.health -= card_c.damage
        elif roundd[1] == card_a.name and card_c.damage < card_a.damage:
            player2.score += 1
            player2.health -= card_c.damage
            player1.health -= card_a.damage
        elif roundd[1] == card_b.name and card_c.damage > card_b.damage:
            player1.score += 1
            player1.health -= card_b.damage
            player2.health -= card_c.damage
        elif roundd[1] == card_b.name and card_c.damage < card_b.damage:
            player2.score += 1
            player2.health -= card_c.damage
            player1.health -= card_b.damage


game(round1)
game(round2)
game(round3)

print(f'{player1.name} -> Score: {player1.score}, Health: {player1.health}')
print(f'{player2.name} -> Score: {player2.score}, Health: {player2.health}')

# result = pd.DataFrame({
#     'player1:': player1.name,
#     'score of player1:': player1.score,
#     'health of player1:': player1.health,
#     'player2:': player2.name,
#     'score of player2:': player2.score,
#     'health of player2:': player2.health
# })
# result.to_csv('result.txt', index=False)
# x = [player1.name, player2.name]
# y = [player1.score, player2.score]
# plt.bar(x, y, color='skyblue')
# plt.xlabel('players')
# plt.ylabel('scores')
# plt.title('Scores Table')
# plt.show()