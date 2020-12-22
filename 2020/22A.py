f = open('Input/22.txt')

decks = [[int(num) for num in section.splitlines()[1:]] for section in f.read().split('\n\n')]

print(decks)

while (len(decks[0]) and len(decks[1])):
    player1_card = decks[0].pop(0)
    player2_card = decks[1].pop(0)
    if player1_card > player2_card:
        decks[0].extend([player1_card, player2_card])
    else:
        decks[1].extend([player2_card, player1_card])

def score(deck):
    score = 0
    for index, card in enumerate(deck[::-1]):
        score += (index + 1) * card
    return score

print("answer:", score(decks[0]) if decks[0] else score(decks[1]))
