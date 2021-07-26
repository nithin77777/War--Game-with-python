import random
suits=['Hearts','Diamonds','Spades','Clubs']
ranks=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace']
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class card():
    def __init__(self,suit,rank):
       self.rank= rank
       self.suit= suit
       self.value= values[rank]

    def __str__(self):
       return self.rank + ' of ' + self.suit



class deck():
    def __init__(self):
        
        self.all_cards= []
        
        for suit in suits:
            for rank in ranks:
                new_cards= card(suit,rank)
                
                self.all_cards.append(new_cards)
                


    def shuffle(self):
        self.shuffle_cards= random.shuffle(self.all_cards)
        
        print(self.shuffle_cards)

    def deal_card(self):
        return self.all_cards.pop()


class player():
    
    def __init__(self, name):
        self.name= name
        self.all_cards= []
        
        
    def add_cards(self,new_cards):
        
        if type(new_cards) == type([]) :
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)
    
    def remove_card(self):
        return self.all_cards.pop(0)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards '

player_one= player('one')
player_two= player('two')

new_deck=deck()
new_deck.shuffle()

for x in range(26) :
    player_one.add_cards(new_deck.deal_card())
    player_two.add_cards(new_deck.deal_card())

#print(player_one.all_cards[0]) ----------> statement optional neglected

game_on= True

round_num= 0

while game_on:
    round_num= round_num + 1
    
    if len(player_one.all_cards)== 0:
        print(str(round_num) + ' rounds played')
        print('Player one loses!, Player two wins!')
        game_on= False
        break
    if len(player_two.all_cards)== 0:
        print(str(round_num) + ' rounds played')
        print('Player two loses!, Player one wins!')
        game_on= False
        break
    
    #New Round
    player_one_cards= []
    player_one_cards.append(player_one.remove_card())
    
    player_two_cards= []
    player_two_cards.append(player_two.remove_card())
    
    #while war-----------------
    at_war= True
    
    while at_war :
        if player_one_cards[-1].value > player_two_cards[-1].value :
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war= False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value :
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            at_war= False
            
        else:
            print('war!')
                       
            if len(player_one.all_cards) < 5:
                print(str(round_num) + ' rounds played')
                print('Player One is not Eligible to play war')
                print('Player two wins!')
                game_on= False
                break
            
            elif len(player_two.all_cards) < 5:
                print(str(round_num) + ' rounds played')
                print('Player Two is not Eligible to play war')
                print('Player one wins!')
                game_on= False
                break
            
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
                   
                    


    

    
    
    

        
        
                
