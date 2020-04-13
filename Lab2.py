from array import *
from random import randint
import random
import numpy as np
import string
#zadanie 2
'''
print('Podaj ile chcesz dodać znaków do tablicy: ')
num = input()
my_array = array('u', [])
for i in range(0,int(num)):
    my_array.append(input('Podaj znak: '))
my_array.reverse()
for i in my_array:
    print(i)
'''
#koniec zadania 2
#zadanie 3
'''
my_array = array('i', [])
for _ in range(10):
    value = randint(0, 10)-5
    my_array.append(value)
print(my_array)
f = open("result.txt", "w")
for i in my_array:
    f.write("{},".format(i))
f.close()
'''
#koniec zadania 3
#zadanie 4
'''
def matrix():
    A = np.array([[2,3,4,5,6],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    for j in range(1,5):
        for i in range(0,5):
            A[j,i] = A[j-1,i] * A[j-1,i]
    
    print(A)

matrix()
'''
#koniec zadania 4
#zadanie 5
'''
def hitogram(file_name):
    myfile = open(file_name, 'r')
    data = myfile.read().replace(" ", "")
    col = []
    for word in data:
        col.append(word)
    return myhist(col)

def myhist(col):
    hist = {}
    for word in col:
        word = word.strip(string.punctuation + string.whitespace)
        hist[word] = hist.get(word, 0)+1
    return hist

col = hitogram('document.txt')
print(col)
'''
#koniec zadania 5
#zadanie 6
class Card:
    def __init__(self,color,ranga):
        self.color = color
        self.ranga = ranga
    def show(self):
        print("{} {}".format(self.ranga, self.color))

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for color in ['Pik','Karo','Kier','Trefl']:
            for ranga in ['2','3','4','5','6','7','8','9','10','Walet','Dama','Król','As']:
                self.cards.append(Card(color,ranga))
    def show(self):
        for d in self.cards:
            d.show()
    def shuffle(self):
        for i in range(len(self.cards) - 1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):
        return self.cards.pop()
class Players:
    def __init__(self,number):
        self.number = int(number)
        self.hand = []
    def DrawAndShow(self,deck):
        for n in range(0,self.number):
            print('\nGracz {}'.format(n+1))
            for i in range(0,5):
                self.hand.append(deck.drawCard())
            
            for card in self.hand:
                card.show()
            self.hand.clear()

deck = Deck()
deck.shuffle()

player = Players(2)
player.DrawAndShow(deck)    
