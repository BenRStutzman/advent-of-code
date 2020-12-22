f = open('Input/22.txt')

decks = [[int(num) for num in section.splitlines()[1:]] for section in f.read().split('\n\n')]

def determine_winner(deck1, deck2):
    previous_states = []
    while (len(deck1) and len(deck2)):
        # print(deck1, deck2)
        if [deck1, deck2] in previous_states:
            return 1, 0
        previous_states.append([deck1[:], deck2[:]])
        player1_card = deck1.pop(0)
        player2_card = deck2.pop(0)
        if len(deck1) >= player1_card and len(deck2) >= player2_card:
            winner, sub_score = determine_winner(deck1[:player1_card], deck2[:player2_card])
        else:
            winner = 1 if player1_card > player2_card else 2
        # print(winner)
        if winner == 1:
            deck1.extend([player1_card, player2_card])
        else:
            deck2.extend([player2_card, player1_card])
    if deck1:
        return 1, score(deck1)
    else:
        return 2, score(deck2)

def score(deck):
    score = 0
    for index, card in enumerate(deck[::-1]):
        score += (index + 1) * card
    return score

print("answer:", determine_winner(decks[0], decks[1])[1])
