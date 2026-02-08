import randomname

def get_riddle(level, index):
    #riddles from https://www.goodhousekeeping.com/life/a41779999/riddles-for-adults/?utm_source=google&utm_medium=cpc&utm_campaign=mgu_ga_ghk_d_bm_prog_org_us_a41779999&gad_source=1&gad_campaignid=18812448934&gclid=Cj0KCQiA-YvMBhDtARIsAHZuUzLajIHBzcGbc3QA3Bd-aZ0YNqnB783TDOkye9Ym4WIXiCx_o4WzbwsaAmQBEALw_wcB
    #https://parade.com/947956/parade/riddles/
    if level == 0:
        return "I'm sweet and cold with a stick to hold; a treat on a hot day, worth more than gold. What am I?"
    
    riddles1 = [
        "I’m tall when I’m young, and I’m short when I’m old. What am I?",
        "The more of this there is, the less you see. What is it?",
        "What gets bigger when more is taken away?"
    ]
    
    riddles2 = [
        "I'm not a blanket, yet I cover the ground; a crystal from heaven that doesn't make a sound. What am I?",
        "What comes down but never goes up?",
        "I have a neck, but no head. I have two arms, but no hands. What am I?",
        "I am easy to lift, but hard to throw. What am I?",
        "The more you take, the more you leave behind. What am I?"
            ]
    riddles3 = [
        "What is black when it’s clean and white when it’s dirty?",
        "What has a head and a tail but no body?",
        "What has one head, one foot and four legs?",
        "It stalks the countryside with ears that can’t hear. What is it?",
        "I am an odd number. Take away a letter and I become even. What number am I?",
        "I have lakes with no water, mountains with no stone and cities with no buildings. What am I?",
        "What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?"
    ]
    if level == 1:
        return riddles1[index]
    elif level == 2:
        return riddles2[index]
    else:
        return riddles3[index]
    

def get_answer(level, index):
    if level == 0:
        return "popsicle"
    answers1 = [
        "candle",
        "darkness",
        "hole"
    ]
    answers2 = [
        "snow",
        "age",
        "shirt",
        "feather",
        "footsteps"
    ]

    answers3 = [
        "chalkboard",
        "coin",
        "bed",
        "corn",
        "seven",
        "map",
        "nothing"
    ]
    if level == 1:
        return answers1[index]
    elif level == 2:
        return answers2[index]
    else:
        return answers3[index]

def welcome_screen():
    print("Welcome dear adventurer to The Throne's Riddle.\n ")#game description
    print("The Throne's Riddle is an interactive questing game that challenges its players\n " +
          "to think deeply about the questions it poses in order to obtain something. \n" +
          "The players are sent by the King and Queen to bring back 1 to 2 items and finally \n"
          "the answer to the King's question. With each question the player is given the riddle \n" +
          "along with the format in which the answer is. Each answer will always be no more than a single word.\n" +
          "Players can answer the riddle as many times as it takes to get to the right answer and \n"+
          "Players can exit the quest by entering 'q' while still saving their progress. \n" +
          "To begin players must decide upon their adventurer name then players must choose between one \n" +
          "which quest they would like to undertake. Quest one, the Treasure Box, requires successful answers to 3 riddles, \n "+
          "quest 2, The Enchanted Necklace, requires successful answers to 5 riddles, and finally the most difficult quest, \n"+
          "The King's answer requires the success of 7 riddles. \n" 
          )
    print("\n\nBy undertaking the Throne's quest you are sharpening your mind in a fun new way. \n")

def choose_name():
    print("\nDear adventurer, please tell me your name\n")
    print("Enter 1 to choose your name and 2 to generate a name\n")
    choice = input()
    
    if choice == str(1):
        print("Tell me, what is your name?: \n")
        name = input()
    elif choice == str(2):
        name = randomname.get_name()
    confirmed = False
    while confirmed != True:
        print("Is "+ name + " your true name? Enter y/n\n")
        true_name = input()
        if (true_name == 'y'):
            confirmed = True
            
        else:
            print("Enter 1 to choose your name and 2 to generate a name\n")
            choice = input()
    
            if choice == str(1):
                print("Tell me, what is your name?: \n")
                name = input()
            elif choice == str(2):
                name = randomname.get_name()
    return name


def tutorial(name):
    welcome_screen()
    #level 0 walk through
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("Riddle Tutorial")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++\n")

    print("\n Each quest asks the player a set number of riddles.\n")
    print("The player must then think deeply and provide an answer to the riddle. \n")
    print("For example you may be asked: \n")
    print(get_riddle(0,0))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    print("The answer to this question is popsicle\n")
    print("Please note that the answer is 'popsicle' not 'a popsicle'\n")
    print("Alright "+name+", you are ready to resume questing.\n"+
          " If you have any difficulties on your journey, please reference this guide again.\n")
    print("\n")


def home_options(progress1, progress2, progress3):
    #choose level or tutorial or quit
    #print current progress
    print("1) Treasure box: "+ str(progress1) + "/3\n")
    print("2) Enchanted necklace: " + str(progress2) + "/5\n")
    print("3) The King's answer: " + str(progress3) + "/7\n")
    print("4) Tutorial \n")
    print("5) Change Name\n")
    print("6) quit")
    print("--------------------------\n")
    print("Enter 1-3 to start/resume a quest, 4 to play the tutorial, 5 to change name, or 6 to quit.\n")
    print("--------------------------\n")
    choice = input()
    return choice

def level1_1(name):
    
    print("You begin your journey with haste and walk for hours. The sun begins to set.\n")
    print("You come upon a small village. The street is empty. The besides the moon, the only light comes peeking through a widowsill.\n")
    print("As you are passing through you hear a rough voice come from beyond the sill, barely above a whispher.\n\nGreetings " + name + ", I have a small query for you if you have but a moment to spare.\n")
    print("\nThe voice continues...\n")
    print(get_riddle(1,0))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(1,0)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what I am... Try again young adventurer.")
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + ", continue on your path.\n")
    return True

def level1_2(name):
    print("As you walk away from the village clouds blanket the sky. You come to a crossroads and notice the silhoutte of a figure sitting by the roadside.\n As you near, the silhoutte calls out to you.\n")
    print("Hello dear traveler, the hour is late. You best make haste. Answer my question and I'll help you on your way.\n\n")
    print(get_riddle(1,1))
    print("\n")
    print("What do you respond? Format: ____\n ('q' to leave)")
    answer = input()
    while (answer != get_answer(1,1) and answer != 'q'):
        print("No, no that's not what it is... Try again young adventurer.")
        print("What do you respond? Format:  ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + ". Take the path on the left. Hurry now, the world shall soon be waking.\n")
    print("With the shrouded figure's words the clouds cleared to illuminate the path. You find yourself alone and continue without looking back\n")
    return True


def level1_3(name):
    print("The sky is beginning to lighten as dawn approaches. The path leads you to a large oak tree with a hollow.\n")
    print("A crow sits perched on the great oak's thickest branch. The crow coos\n")
    print("You've come a long way this short night. I wish to help end your journey here\n")
    print(", but first you must answer just one question for me.\n\n")
    print("Tell me "+ name+", ")
    print(get_riddle(1,2))
    print("\n")
    print("What do you respond? Format: A ____ ('q' to leave)\n")
    answer = input()
    while (answer != get_answer(1,2) and answer != 'q'):
        print("No, no that's not what it is... Try again young adventurer.")
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + " the crow responds. The takes flight and disappears into\n")
    print("With the shrouded figure's words the clouds cleared to illuminate the path. You find yourself alone and continue without looking back\n")
    print(" into the hole of the tree. You peer inside and see an old and battered\n")
    print(" wooden box. After fishing it out you open the box. Inside is a blue diamond brooch exquistly set in gold.\n")
    print("You've completed your journey and present the treasure to the King.\n")
    return True

def progress_label(quest, progress, max):
    print("\n===========================\n")
    print(quest+": "+ str(progress +1) +"/"+ str(max)+"\n")
    print("===========================\n\n")

def level1(progress, name):
    #play level one and return progress
    #display progress
    if (progress == 0):
        progress_label("Treasure Box Quest", progress, 3)
        if (level1_1(name) == True):
            progress = 1

    if (progress == 1):
        progress_label("Treasure Box Quest", progress, 3)
        if (level1_2(name) == True):
            progress = 2

    if (progress == 2):
        progress_label("Treasure Box Quest", progress, 3)
        if (level1_3(name) == True):
            progress = 3
        
        

    return progress
    
    
def level2_1(name):
    print("You begin your journey with haste and walk for hours. The air begins to turn chilly.\n"+
          "On the path you meet a young child wrapped in a cloak. The child glances up at you.\n"+
          "You reach into your pocket to retrieve a coin for the child, but they respond \n"+
          "no thank you "+name+" I have no need for such things. Please show me your kindess by \n"+
          "answering a small quiery. They go on...\n"
          )
   
    print(get_riddle(2,0))
    print("\n")
    print("What do you respond? Format: ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(2,0)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what I am... Try again "+name)
        print("What do you respond? Format:  ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + ", continue on your path. You are only at the begining of your journey.\n")
    return True

def level2_2(name):
    print("Next, you come to a village. Within the village is an old man in battered clothing. \n"+
          "He gazes at you with kind eyes. You've come on a noble quest he says. \n"+
          "My days of adventure have long since passed. But I hope I may I be of some help to you. \n"+
          "To continue on your way answer me this: \n"
          )
   
    print(get_riddle(2,1))
    print("\n")
    print("What do you respond? Format: ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(2,1)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what it is... Try again "+name)
        print("What do you respond? Format:  ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right young one. Hurry along now. Time waits for no one.\n")
    return True

def level2_3(name):
    print("Futher down the road you meet a trader roaming with their wares.\n"+
          "You stop to purchase a small snack.\n"+
          "The trader says rather than money, pay with your wisdom. Please tell me: \n"
          )
   
    print(get_riddle(2,2))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(2,2)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what I am... Try again "+name)
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + ", take this food and continue on your way.\n")
    return True

def level2_4(name):
    print("A humming bird of a virbrant green hue  circles you.\n"+
          "The humming bird says to you: Hello adventurer! I have heard that you are\n"+
          "on a grand quest. You are nearing its end now so please answer me this: \n"
          )
   
    print(get_riddle(2,3))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(2,3)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what I am... Try again "+name)
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + "! That's right! Your desires are almost in reach! Go on now! And the humming bird zips away.\n")
    return True

def level2_5(name):
    print("You have walked a very long way and have grown tired. You see a stream and go to sit beside it\n"+
          "A deer comes up beside you as you rest and looks to you. It says My, My how far you have come. \n"+
          "The soles of your shoes have become worn and your eyes have started to close. \n"+
          "It is time for you to end your journey, but first prove yourself with just one final question.\n"
          )
   
    print(get_riddle(2,4))
    print("\n")
    print("What do you respond? Format: ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(2,4)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what I am... Try again "+name)
        print("What do you respond? Format:  ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + ", now look at all you've accomplished. \n")
    print("The deer nods back towards the way you came. In your the outline of \n" +
          "your footsteps you see something sparkle in the dirt. It is the enchanted" +
          "you have been searching for. You take it and present it to the throne, completing\n"+
          "your the quest of the Enchanted Necklace."
          
          )
    return True

def level2(progress, name):
    #play level two and return progress
    if (progress == 0):
        progress_label("Enchanted Necklace Quest", progress, 5)
        if (level2_1(name) == True):
            progress = 1

    if (progress == 1):
        progress_label("Enchanted Necklace Quest", progress, 5)
        if (level2_2(name) == True):
            progress = 2

    if (progress == 2):
        progress_label("Enchanted Necklace Quest", progress, 5)
        if (level2_3(name) == 1):
            progress = 3
        
    if (progress == 3):
        progress_label("Enchanted Necklace Quest", progress, 5)
        if (level2_4(name) == True):
            progress = 4

    if (progress == 4):
        progress_label("Enchanted Necklace Quest", progress, 5)
        if (level2_5(name) == True):
            progress = 5

    return progress
   
def level3_1(name):
    print("The King had a dream that posed a question of great significance to the kingdom.\n"+
          "It is said that the answer that lies at the end of your journey will be identical \n"+
          "to that of the answer to the question in the King's dream. \n"+
          "You begin your quest to seek the all important answer.\n "+
          "You begin to walk down a dirt path and come upon a group of children\n "+
          "outside a schoolhouse. One of the children runs up to you saying mister, mister"+
          "I have a question for you. The child continues.."
          )
   
    print(get_riddle(3,0))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(3,0)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what it is... Try again "+name)
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + "! Thank you! Bye Bye!\n")
    print("You continue down the path.\n")
    return True

def level3_2(name):
    print("You later come upon a well. Peering into the well a voice calls out ot you.\n"+
          "Young and wise adventurer I have a question for you.\n"
          )
   
    print(get_riddle(3,1))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(3,1)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what it is... Try again "+name)
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + ". Get going, get going for something\n"+
          "greater than riches await you.")
    return True
    

def level3_3(name):
    print("The sun is setting now. You stop at an inn and enter inside.\n"+
          "A bard is playing music. You approach the woman at the counter\n"+
          "and ask for a room. I have just one room left and it is yours \n"+
          "for the night granted you can answer just one question from me."
          )
   
    print(get_riddle(3,2))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(3,2)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what I am... Try again "+name)
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + ", take rest so that you may awake with\n"+
          "the sun and continue your journey tomorrow.\n")
        
    return True

def level3_4(name):
    print("You rise feeling rested and continue on your path. You walk and walk\n"+
          "Until you come to a farm. At the farm a scarecrow stands at attention.\n"+
          "The scarecrow calls out to you, Hello "+name+" the crows have been\n"+
          "chattering away about you. They call you the wisest of them all.\n"+
          "I am quite skeptical of these silly crows words. To prove yourself\n" +
          "answer something so very simple: \n"

          )
   
    print(get_riddle(3,3))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(3,3)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what it is... Try again "+name)
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's correct " + name + ". I suppose the rumors have truth.\n"+
          "You best not dally, for the kingdom depends on you.")
    return True

def level3_5(name):
    print("You walk futher down the path and encounter another village.\n"+
          "The village has an outdoor market that you wander through\n"+
          "At a stall selling pies the shopkeeper calls out to you, \n"+
          "Youngin, yes you there, I have a question that I must pose to you: \n"
          )
   
    print(get_riddle(3,4))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(3,4)
    while (answer != truth and answer != 'q'):
        print("No, no that cannot possibly be it... Try again "+name)
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + "! Here take a pie with you as you complete your trials.\n")
    return True

def level3_6(name):
    print("Moving away from the town you meet another traveler.\n"+
          "The traveler stops you, stating A journey far a journey wide\n"+
          "you have come a long way, and so have I. With sore legs and a\n"+
          "thirst for sights of grander I ask you this.\n"
          )
   
    print(get_riddle(3,5))
    print("\n")
    print("What do you respond? Format: A ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(3,5)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what I am... Try again "+name)
        print("What do you respond? Format: A ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("That's right " + name + ". You have true understanding of the world \n"+
          "and beyond. Just one step futher and you have acheived something greater\n")
    return True

def level3_7(name):
    print("With renewed viger you push forward. With the rustling of the wind\n"+
          "you hear WHOOOO from the hollow of a tree. From the tree an owl calls out\n"+
          name+ " I have been waiting for you, watching you grow. Your wisdom\n"+
          "is unbounded and your temper calm. To be the hero this kingdom needs\n"+
          "I beseech you, lend your thoughts one again to this riddle.\n"
          )
   
    print(get_riddle(3,6))
    print("\n")
    print("What do you respond? Format: ____\n ('q' to leave)")
    answer = input()
    truth = get_answer(3,6)
    while (answer != truth and answer != 'q'):
        print("No, no that's not what I am... Try again "+name)
        print("What do you respond? Format: ____ ('q' to leave)\n")
        answer = input()
        if answer == 'q':
            return False
    if answer == 'q':
        return False
    print("You've shown your greatness " + name + ". Let no more be saide \n"+
          "The owl flies off. You return to the King and Queen. The King stands"+
          "From his throne and walks to stand face to face with you. Tell me\n"+
          "wise adventurer, tell me the answer this kindom seeks.\n"+
          "You answer the king, I must answer nothing. A murmer spreads throughout\n"+
          "the court. The King responds simply with, I see.\n"+
          "Your journey is done wise one. Thank you truely. He returns to this throne\n"+
          "and you leave for some rest.\n"
          )
    return True



def level3(progress, name):
    #play level three and return progress
    if (progress == 0):
        progress_label("King's Answer Quest", progress, 7)
        if (level3_1(name) == True):
            progress = 1

    if (progress == 1):
        progress_label("King's Answer Quest", progress, 7)
        if (level3_2(name) == True):
            progress = 2

    if (progress == 2):
        progress_label("King's Answer Quest", progress, 7)
        if (level3_3(name) == 1):
            progress = 3
        
    if (progress == 3):
        progress_label("King's Answer Quest", progress, 7)
        if (level3_4(name) == True):
            progress = 4

    if (progress == 4):
        progress_label("King's Answer Quest", progress, 7)
        if (level3_5(name) == True):
            progress = 5

    if (progress == 5):
        progress_label("King's Answer Quest", progress, 7)
        if (level3_6(name) == True):
            progress = 6

    if (progress == 6):
        progress_label("King's Answer Quest", progress, 7)
        if (level3_7(name) == True):
            progress = 7

    return progress

def play_game():
    progress1 = 0
    progress2 = 0
    progress3 = 0
    welcome_screen()
    name = choose_name()
    user_choice = home_options(progress1, progress2, progress3)
    end = False
    while (end == False) and (progress1 < 3 or progress2 < 5 or progress3 < 7):
        if (user_choice == '1') and (progress1 < 3):
            progress1 = level1(progress1, name)
        elif (user_choice == '2') and (progress1 < 5):
            progress2 = level2(progress2, name)
        elif (user_choice == '3') and progress3 < 7:
            progress3 = level3(progress3, name)
        elif (user_choice == '4'):
            tutorial(name)
        elif (user_choice == '5'):
            name = choose_name()
        elif (user_choice == '6'):
            print("Are you certain you would like to quit The Throne's Riddle\n")
            print("Any quest progress you have made will be lost. Enter y/n\n")
            leave = input()
            if leave=='y':
                end = True        
        else:
            print("Invaild input. Please Enter valid choice.\n")
        if (end != True):
            user_choice = home_options(progress1, progress2, progress3)
    
    if (progress1 == 3 and progress2 == 5 and progress3 == 7):
        print("\nCongrationations " +name +" you have successfully "+
              "completed The Throne's Riddle.\n") #congrats on finishing game and getting ultimate reward  
    
    
    if (user_choice == 6):
        print("Goodbye " + name + ", I hope you enjoyed your adventure.")
    


play_game()     
   










        
    
