```
______ _            _      ___            _      _    _ _                  _ 
| ___ \ |          | |    |_  |          | |    | |  | (_)                | |
| |_/ / | __ _  ___| | __   | | __ _  ___| | __ | |  | |_ ______ _ _ __ __| |
| ___ \ |/ _` |/ __| |/ /   | |/ _` |/ __| |/ / | |/\| | |_  / _` | '__/ _` |
| |_/ / | (_| | (__|   </\__/ / (_| | (__|   <  \  /\  / |/ / (_| | | | (_| |
\____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_\  \/  \/|_/___\__,_|_|  \__,_|
```

## Malek Yehya
## CMSI 1010
## 7 November 2025
## Final Project Proposal Draft


The goal of this project is to create a black jack simulator with pixel art gui that allows for betting, splitting, doubling down, and maybe side bets. 
It will have one player and they will play against the house so a total of two hands. There will be a wizard which when clicked on will display a chat bubble or something that shows what the book suggests.
The book will be entered using nested dictionaries and will run in the backround for every had but it will only be displayed if you click on the wizard sitting next to you.
There will maybe be music depending on if using creative common assets is allowed. The planned python libraries are going to be pygame and random. The art will be made using Aesprite since I already have a license.

The core functionality of the project is designed to be pretty simple and will be broken down as such:

### Core Functionality

For the raw gameplay code there will likely be one class **Hand** with child classes of **Player**, **House**, and **Wizard**. The **Hand** class will define the core functionality of each hand such as dealing the cards
and adding up the totals. It will also define the winning conditions that are constant for each side (ie. Does **Player** total beat **House** hand and does either bust out). The **Dealer** child class will inherit 
all the functions that define a black jack hand (ie. Two cards are dealt at first and such). The **Dealer** class will have its own functions that define the strategy (ie. Hit soft 17 and stand on 17) as well as ensure that 
cards are displayed properly (one face down on initial deal and it is turned over after hand is complete if conditions are met). The **Player** child class will be the most complicated and will recieve the inputs 
and then perform actions that are part of the Player's available strategy. If the player wants to double down on 20 they can, stuff like that. The **Player** class will also inherit the core functions that define a hand
like initial deal and bust amount from the **Hand** parent class. The **Wizard** class is just going to take into account the dealer and player hands and use those to determine the play by the book strategy. If i have lots
of time i might include enough scenarios in the nested dictionary to handle strategy after the first deal but that is only if I finish minimum functionality.

### Dependencies
1. Pygame
2. Random

### Order of Development Workflow

1. The first step is making a gameplay loop that runs in the console. This is to prove that the core gameplay works and has a minimum functionality. I am unsure if **Wizard** functionality will be prioritized here. 
(it might be the last thing I focus on)

2. The second step is making a barebones gui that displays placement art so I can wire up the gameplay to the gui. If this step is complete then I can work on the **Wizard** functionality alongside the art process 
(my art is going to be so shit but I think it will add to the fun of the game). 

3. This is the fun part now I put all the art together to make this game look pretty. Hopefully I can figure out a easy way to fully buildout the **Wizard** functionality but that might be tedious based on my previous experience
with super large and complicated nested dictionaries and parsing through them to get specific keys.

4. Assuming the art is finished and I still have time then I can work on the **Wizard** full time as well as any finishing touches. Since I will be working in a git repo **Wizard** will always be on a separate branch then main 
until it is fully fleshed out.

5. Play some blackjack and enjoy my work. 

### Controls

The primary way of playing the game is going to be through the keyboard since the first state of development will be isolated to the console. However after the GUI is made there will be button functionality that allows the 
player to use the cursor to navigate and click on buttons to perform actions such as hit, split or double down as well as access the menu. This cursor fucntionality will be prioritized alongside the art however 
**ART WILL ALWAYS HAVE PRIORITY** since we will already have controls mapped to the keyboard.

### Art

The art will be drawn in Aesprite and there will be two categories of art. Fixed art which will be buttons and background objects that will stay in the same place the whole time in the game. Static elements that can 
have cursor or keyboard interaction will have a element that either changes the opacity or color or enlarges the size when selected or hovered over. If cursor functionality is dropped you will be able to navigate through 
options such as the menu with the arrow keys. This functionality will liekly be included alongside cursor functionality if that is developed.

The main sprite that will have true animations is just the cards. This will be tricky and i don't know exactly how i am going to do it until i determine the screen size and the size of the other static elements. 
The goal is to have a deal animation that can be used for any deal including the intial deal of both hands. Then there will be a card organization animation that arranges the cards in a fashion that both conserves screen 
space while maintaining readaility. This will take some fine tuning to ensure that hands that end up with many cards will have ample screen real estate. The way I envision this working is the card size never changes instead 
we move the cards together so that the top left pip and number are showing. This functionality may be adjusted or dropped or limited by something like split amount limits (you can only split twice or something like that).

Currently I am planning on having a defined screen size that will not change but it will be pretty large. This will allow me to scale the background and static elements so they look nice and are also properly drawn in terms 
of the pixels available on the display size i choose. I will make the screen size large enough so that I ensure that the animation of the cards dealing and adjusting fit in the worst case scenarios. There will likely be no 
screen adjustments since that is an edge case I don't want to handle.

Ideally I make all the art in a defined size determined by pixels so centering and moving stuff around is simple. Then I don't have to worry about lots of edge cases as long as I plan out in detail the art.
