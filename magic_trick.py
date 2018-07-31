
suit=['Spades', 'Hearts', 'Clubs', 'Diamonds']
value=['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
cards=[]
props={}
reacurring_rank=[]
weighed={}
def pick_random_card():
    global cards
    import random
    card=value[random.randrange(len(value))]+'_'+suit[random.randrange(len(suit))]
    if card in cards: return pick_random_card()
    else: return card ## picks a random card by the given parameters above
# # WARNING: SPOILERS! # IDEA:
# #      - draw 5 cards arbitrarily
# #      - atleast one card's rank will double inevitably (5 cards drawn - 4 available ranks)
# #      - one card with doubled rank has to be first(which one will be elaborated shortly)
# #      - imagine a continues cycle with all values ranging from ace to king, where ace is one and king is 13
# #      - you read this template clockwise
# #      - now the distance ranging between the cards with same rank gets examined
# #      - the shorter distance gets purposely chosen (max distance is 6);
# #      - the established distance gets portrayed hiddenly by aranging the left overcards next
# #      - while the system can be adjusted, I chose mine to be:
# #           -(S, M, L)=1; (S, L, M)=2; (M, S, L)=3; (M, L, S)=4; (L, S, M)=5; (L, M S)=6 (3! possibilities)
# #      - Now resulting is a clear system where it is clear what the missing card is. Enjoy!
# #______________________________________________________________________________

def find_reacurring_rank():
    for i in props:
        for j in props:
            if i!=j:
                if props[i][1]==props[j][1]:
                    return [i, j]

def find_distance(s, v):
    global card_to_show, card_to_hide
    dist=0
    index=0
    card_to_show=s
    card_to_hide=v
    while value[index]!=props[s][0]:
        index+=1
    while value[index]!=props[v][0]:
        if index>=len(value)-1:
            index=0
        else:index+=1
        dist+=1
    if dist>6:
        dist=13-dist
        card_to_show,card_to_hide=card_to_hide,card_to_show
    return dist

def weight():
    weighed={}
    set={}
    for i in range(len(cards)):
        if i!=card_to_show and i!=card_to_hide:
            set[cards[i]]=i
    weights={
        'Ace':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '10':10,
        'Jack':11,
        'Queen':12,
        'King':13
    }
    for i in set:
        bar=i.split("_")
        weighed[weights[bar[0]]]=i
    return weighed
def order(dist):
    global card_to_show, card_to_hide, weighed
    options={
        1: [0, 1, 2],
        2: [0, 2, 1],
        3: [1, 0, 2],
        4: [1, 2, 0],
        5: [2, 0, 1],
        6: [2, 1, 0]
    }
    order=options[dist]
    result=cards[card_to_show]+" "
    used=[]
    for i in range(len(order)):
        foo=0
        for j in range(14):
            if j in weighed:
                if foo==order[i]:
                    result+=weighed[j]+" "
                foo+=1
    return result
def main():
    global cards, suit, value, card_to_hide, card_to_show, props, weighed
    for i in range(5):
        cards.append(pick_random_card()) ##equivalent of drawing 5 cards at random
    result=""
    for card in cards:
        result+=card+" "
    print(result)
    answer=input('Another Draw? y/n: ')
    if answer.lower()=='y':
        while len(cards)>0:
            cards.pop()
        return main()
    for i in range(101):
        print('\n')
    props={x:cards[x].split("_") for x in range(len(cards))} ## a set of the properties of each card
    card_to_show=0
    card_to_hide=0
    reacurring_rank=find_reacurring_rank() ## establishes the doubled rank
    s,v=reacurring_rank[0],reacurring_rank[1]
    dist=find_distance(s,v) ## returns shortest possible distance between the cards value
    weighed=weight()
    print(order(dist)+"\n\n\nI Wonder What the Missing Card is though?") ## returns the order the cards are layed out(obvioulsy without the hidden card)
    input("\n\n\nReveal?\n\n\n")
    print(cards[card_to_hide]+"\n\n**MAGIC!**")
    return
#____________________________________________________________
main()
