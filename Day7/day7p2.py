file = open("day7input")
scoreOrder = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
scoreOrder.reverse()
cards = []
cardCount = 0
for line in file:
    lineSplit = line.split(" ")
    cards.append({"card":lineSplit[0],"bid":lineSplit[1].strip()})

def cardorder(card):
    return scoreOrder.index(card)


def firstcard(card):
    return scoreOrder.index(card['card'][0]),scoreOrder.index(card['card'][1]),scoreOrder.index(card['card'][2]),scoreOrder.index(card['card'][3]),scoreOrder.index(card['card'][4])

fiveOAK=[]
fourOAK=[]
fullHouse=[]
threeOAK=[]
twoPair=[]
onePair=[]
highCard=[]


for card in cards:
    cardCopies = list(card['card'])
    cardCopies.sort(key=cardorder,reverse=True)
    cardMatch=0
    cardIndex=0
    seenCards = []
    cardCounts=[]
    print(cardCopies)
    if cardCopies.count("J") > 0:
        for cardCopy in cardCopies:
            if cardCopy not in seenCards:
                if cardCopy != "J":
                    cardCounts.append(cardCopies.count(cardCopy))
                    seenCards.append(cardCopy)
        cardCounts.sort()
        if len(cardCounts) > 0 :
            cardCounts.append((cardCounts.pop() + cardCopies.count("J")))
        else:
            cardCounts=[5]
    else:
        for cardCopy in cardCopies:
            if cardCopy not in seenCards:
                cardCounts.append(cardCopies.count(cardCopy))
                seenCards.append(cardCopy)
        cardCounts.sort()


    print(cardCounts)
    match(cardCounts):
        case([5]):
            fiveOAK.append(card)
        case([1,4]):
            fourOAK.append(card)
        case([2,3]):
            fullHouse.append(card)
        case([1,1,3]):
            threeOAK.append(card)
        case([1,2,2]):
            twoPair.append(card)
        case([1,1,1,2]):
            onePair.append(card)
        case([1,1,1,1,1]):
            highCard.append(card)

fiveOAK.sort(key=firstcard, reverse=True)
fourOAK.sort(key=firstcard, reverse=True)
fullHouse.sort(key=firstcard, reverse=True)
threeOAK.sort(key=firstcard, reverse=True)
twoPair.sort(key=firstcard, reverse=True)
onePair.sort(key=firstcard, reverse=True)
highCard.sort(key=firstcard, reverse=True)

cards = []
cards.extend(fiveOAK)
cards.extend(fourOAK)
cards.extend(fullHouse)
cards.extend(threeOAK)
cards.extend(twoPair)
cards.extend(onePair)
cards.extend(highCard)
print(cards)
cards.reverse()
cardCount = 1
total = 0

for card in cards:
    total += int(card["bid"]) * cardCount
    cardCount += 1
print(total)
