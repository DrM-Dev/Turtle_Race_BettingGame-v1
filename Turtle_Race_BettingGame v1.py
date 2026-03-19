#Turtle Race BettingGame v1  by  Dr.M-Dev:
#====================================================================================
#====================================================================================
# Imports__________________________:>
from turtle import Turtle, Screen
import random





print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')


print("******** WELCOME TO Turtle Race BettingGame v1  -   By: Dr.m DEV *********")
#==========================================================================================================
#______________________________________________________________

#__________________________________Main Objects & Classes
#SCREEN
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Turtle_Race_BettingGame v1")
my_screen.bgcolor("black")
#TURTLE - Instances:
tim_clone1 = Turtle(shape="turtle") #Adding pre-made ATTRIBUTES to set up the DEFAULT for every turtle in the race xD
tim_clone2 = Turtle(shape="turtle")
tim_clone3 = Turtle(shape="turtle")
tim_clone4 = Turtle(shape="turtle")
tim_clone5 = Turtle(shape="turtle")
tim_clone6 = Turtle(shape="turtle")
tim_clone7 = Turtle(shape="turtle")
#
race_referee = Turtle(shape="arrow")
race_referee.hideturtle()

#___________________________________Default Race-Modeling List:
timmies = [tim_clone1,tim_clone2,tim_clone3,tim_clone4,tim_clone5,tim_clone6,tim_clone7]
timmies_colors = ["pink","red","orange","yellow","green","blue","purple"]
color_num = 0
y_position = 150
unified_shape = "turtle"
#|#|#|#|#|#|#|#|#
#====================================================================================
#====================================================================================
#DRAWING THE RACE BORDER! & Arranging Turtles
for turtles in timmies:
    turtles.penup()
    turtles.color(timmies_colors[color_num])
    turtles.goto(-200,y_position)
    turtles.shape(unified_shape)
    #
    color_num +=1
    y_position -= 50
#
#
#------------------------
race_referee.color("white")
race_referee.hideturtle()
race_referee.speed(10000)
#
race_referee.penup()
race_referee.goto(240,200)
race_referee.showturtle()
race_referee.pendown()
race_referee.goto(240,-200)
race_referee.hideturtle()


#====================================================================================
#====================================================================================
#_________________________________Betting-line:
race_is_on = False
the_winning_turtle = ""
#
user_bet = my_screen.textinput(title="LET'S GO BETTING!", prompt="Type the name of the color for the turtle you bet on: ").lower()

if user_bet != "":
    race_is_on = True

#_________________
dedicated_speed_gatcha = []
for numbers in range(10,20):
    dedicated_speed_gatcha.append(numbers)
#_________________
winner = None
#_________________
while race_is_on:
    for racers in timmies:
        random_speed = random.choice(dedicated_speed_gatcha)
        racers.forward(random_speed)
        #_______THE WIN SCANNER:
        racer_signature = racers.pos()
        distance = racer_signature[0]
        if distance >= 240:
            print(
                ''' #__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__#''')

            print(
                ''' #__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__#''')

            ##########################
            print(f"{racers.color()[0]} WON!!!!🏁")
            ###########################
            winner = racers.color()[0]
            race_is_on = False
            #
            the_winning_turtle = racers
            break

race_finals = ""
################
if user_bet == winner:
    #-----------#
    print("YOU WON :O🏁")
    print(''' #__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__#''')
    print(''' #__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__#''')
    #
    my_screen.textinput("🎉YOU WON!!!!🏁", prompt=f"the turtle you picked [{user_bet}] won the race :)")


else:
    # -----------#
    print("you lost :<")
    print(''' #__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__#''')
    print(''' #__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__##__#''')
    #
    my_screen.textinput("you lost :<", prompt=f"the turtle you picked [{user_bet}] lost the race :(")


#====================================================================================
#_____________________END CODE
my_screen.exitonclick()
