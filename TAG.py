import time
global weapon
weapon="0"

def hero_path(): 

    print(r"""

                         

  _    _                _       _____      _   _     _ 
 | |  | |              ( )     |  __ \    | | | |   | |
 | |__| | ___ _ __ ___ |/ ___  | |__) |_ _| |_| |__ | |
 |  __  |/ _ \ '__/ _ \  / __| |  ___/ _` | __| '_ \| |
 | |  | |  __/ | | (_) | \__ \ | |  | (_| | |_| | | |_|
 |_|  |_|\___|_|  \___/  |___/ |_|   \__,_|\__|_| |_(_)
                                                       
                                                       

                              
                               

""")
    time.sleep(2)
    print("It has been a long and hard journey back to Gotham Village,\n")
    time.sleep(2)
    print("But you know all of your training has led to this.\n")
    time.sleep(2)
    print ("You see there is a notice board near Solomon Forest,\n")
    time.sleep(2)
    print("There is a quest nailed to the board from Sheriff Gordon about a missing Princess\n")
    time.sleep(2)
    print("Do you want to help in saving this Princess?\n")
    time.sleep(2)
    note_post=(input("Enter '1' for Yes or '2' for No: ")).lower()
    if note_post == ("1"):
        print("\nYou choose to save the missing Princess from a beast in the Arkham Castle.\n")
        time.sleep(2)
        print("You head down towards the forest to find a path.\n")
        time.sleep(2)
        forest_path()
    elif note_post==("2"):
        print("\nThe adventurer ignores the quest to help and goes on their way, never knowing the adventure that could have been.\n")
        time.sleep(2)
        print("Nope, you don't get away THAT easily.\n")
        time.sleep(2)
        hero_path()
    else:
        print("Sorry, I didn't understand that. Please try again\n")
        time.sleep(2)
        hero_path()

def forest_path():
    print("You enter Solomon Forest, it's dark and cold and you feel eyes on you as you travel through it.\n")
    time.sleep(2)
    print (r"""
                         .
                                              .         ;  
                 .              .              ;%     ;;   
                   ,           ,                :;%  %;   
                    :         ;                   :;%;'     .,   
           ,.        %;     %;            ;        %;'    ,;
             ;       ;%;  %%;        ,     %;    ;%;    ,%'
              %;       %;%;      ,  ;       %;  ;%;   ,%;' 
               ;%;      %;        ;%;        % ;%;  ,%;'
                `%;.     ;%;     %;'         `;%%;.%;'
                 `:;%.    ;%%. %@;        %; ;@%;%'
                    `:%;.  :;bd%;          %;@%;'
                      `@%:.  :;%.         ;@@%;'   
                        `@%.  `;@%.      ;@@%;         
                          `@%%. `@%%    ;@@%;        
                            ;@%. :@%%  %@@%;       
                              %@%%%%%%%%%:;     
                                #@%%%%%%%'
                                %@@%%%%%%
                                %@@@%@@@@  . '         
                                %@@@@@@@@         
                            `.. @@@@@@@@@         
                               `@@@@@@@@@        
                                @@@@@@@@@        
                               .@@@@@@@@@         
                               ;@@@@@@@@@.          
                              ;%@@@@@@@@@@. 
                          ___;%@@@@@@@@@@@@,__
""")
    time.sleep(2)
    print("You come to three paths.\n")
    time.sleep(2)
    print("You must choose wisely.\n")
    time.sleep(2)
    forest_path1= (input("Enter '1' for Path One.\nEnter '2' for Path Two.\nEnter '3' for Path Three.\nWhich one will you choose? "))
    if forest_path1 == ("1"):
        print("\nYou travel for what feels like hours through the dark forest,\n")
        time.sleep(2)
        print("You eventually exit and see Arkham Castle near by.\n")
        time.sleep(2)
        door_choice()
    elif forest_path1== ("2"):
        print("\nThe path twists and turns but you exit to see a tavern,\n")
        time.sleep(2)
        print("The tavern is a seedy place but you may find information here.\n")
        time.sleep(2)
        tavern_intro()
    elif forest_path1==("3"):
            print("\nYou are never seen again,\n")
            time.sleep(2)
            print("Some people say Grundy got them but no one dares to enter the forest to find out.\n")
            time.sleep(2)
            print("Please try again the adventure must continue.\n")
            time.sleep(2)
            game_over()
    else:
        print("Sorry I didn't understand that, please try again")
        time.sleep(2)
        forest_path()

def tavern_intro():
    print("You have entered the tavern and notice two people.\n")
    time.sleep(1.5)
    print("A man at a table and a Bar keeper.\n")
    time.sleep(1.5)
    print("Do you want to talk to the man at the table or the Bar keeper? \n" )
    choose_individual()
        
def choose_individual():
    individual=int(input("Enter '1' to approach the man at the table or '2' for the Bar keeper: "))
    if individual == (1):
        print("\n\"I see you've read the notice board....I've got information that might help you. Do you want this information?\"\n")
        time.sleep(2)
        answer=int(input("Enter '3' for Yes and '4' for No: "))
        if answer == (3):
            print("\n\"You will find a hammer on your travels and I'm sure you could put it to good use\"\n")
            time.sleep(3)
            print("You thank him for the information, stand up and walk back out of the door\n") 
            time.sleep(2.5)
            forest_path()
        elif answer==(4):
            print("\nFine then, I'll keep the information to myself.\n")
            time.sleep(2)
            print("You stand up and walk back out of the door\n")
            time.sleep(2)
            print("You foolish nave, do you think you can win this game without information? The answer is NO\n")
            time.sleep(3)
            game_over()
        else:
            print("...\n")
            time.sleep(2)
            tavern_intro()  
    elif individual == (2):
        print("\n\"I hear you are on a quest.\" \n")
        time.sleep(2)
        print("\"I know a man who has worked at the castle.\"\n")
        time.sleep(2)
        print("\"You need to talk to him.\"\n")
        time.sleep(2)
        print("Do you want to talk to the Cloaked Stranger?\n")
        man=input("Enter '1' to talk to the Cloaked Stranger or '2' if you don't want to. ")
        if man.lower().strip()=="1":
            print("\nYou sit across from the Stranger in the cloak made of heavy dark fabric with intricate embroidery.\n")
            time.sleep(2)
            print("The cloaked stanger keeps his head down, the hood of his cloak covering his head and hiding his face.\n")
            time.sleep(2)
            print("\"Another one on this path...\" says the cloaked stranger\n")
            time.sleep(2)
            print("\"You're looking for information, I can tell\"\n")
            time.sleep(2)
            print("\"Be wise with your choice. A sharp blade and balanced handle will be your friend.\"\n")
            time.sleep(2)
            print("You thank him for the information, stand up and walk back out of the door")
            time.sleep(2)
            return_path()
        elif man.lower().strip()== "2":
            print("Scared of him? Loser\n")
            time.sleep(2)
            print("You die a slowwwwww coward's death\n")
            time.sleep(2)
            game_over()
    else:
       choose_individual()
        
def door_back():
    print("You go back to the 2 other doors\n")
    time.sleep(2)
    door = input("Choose a Door number:\n2 Door 2\n3 Door 3\n")
    if door == "2":
            return_path()
    elif door == "3":
            print ("You walk towards the door and open it\n")
            time.sleep(2)
            ending(weapon)
    else:
            print ("You enter an incorrect option.\n Please try again\n")
            time.sleep(2)
            door_back()

def door_choice ():
    print("You enter the Arkham Castle\n")
    time.sleep(2)
    print("You start walking down a large long hall where you see three doors\n")
    time.sleep(2)
    door = input("Choose a Door number:\n1 Door 1\n2 Door 2\n3 Door 3\n")
    if door == "1":
       weapon_choice()
    elif door == "2":
        return_path()
    elif door == "3":
        print ("You walk towards the door and open it\n")
        time.sleep(2)
        ending(weapon)
    else:
        print ("You enter an incorrect option.\n Please try again\n")
        time.sleep(2)

def weapon_choice():
    global weapon
    weapon = input("You enter the Armory of Arkham Castle\n Which weapon do you want to pick up?\n1 Sword\n2 Hammer\n3 Magic Wand\n")
    if weapon == "1":
        print ("You pick up the sword and go back through the door.\n")
        time.sleep(2)
        print (r"""
                                       / | \ 
                                     /   |   \ 
                                    /    |    \ 
                                    |    |    | 
                                    |    |    | 
                                    |    |    | 
                                    |    |    | 
                                    |    |    | 
                                    |    |    | 
                                    |    |    | 
                                    |    |    | 
                                    |    |    | 
                                    | .·´|`·. | 
                                    |;::;|;::;| 
                                    |;::;|;::;| 
                                    |;::;|;::;| 
                                    |;::;|;::;| 
                                    | .·´¯`·. | 
                                    |;       ;| 
                                    |'`·._.·´'| 
                                    |;::;|;::;| 
                        |¯`·._.·´¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯`·._.·´¯| 
                        |                                 | 
                        |_________________________________| 
                        |.·´¯`·.___             ___.·´¯`·.| 
                                    .·´      `·.     
                                    |.·´¯`·..·´| 
                                    |`·._.·´`·.| 
                                    |.·´¯`·..·´| 
                                    |`·._.·´`·.| 
                                    |__________| 
            
               """)
        time.sleep(2)  
        door_back()
    elif weapon == "2":
        print ("You pick up the hammer and go back through the door.\n")
        time.sleep(2)
        print(r"""
                                              ^
                  .--------------.___________) \       
                  |//////////////|___________[ ]   
                  `--------------'           ) (      
                                             '-'      
  """)
        time.sleep(2)
        door_back()
    elif weapon == "3":
        print ("You pick up the Magic Wand and go back through the door.\n")
        time.sleep(2)
        door_back()
    else:
        print("This weapon is not available")
        time.sleep(2)
        weapon_choice()

def return_path():
        print ("You open the door and enter a small grotto which leads you back to the forest\n")
        time.sleep(2)
        forest_path()

def generic_ending():
    print("You enter a cavernous room that has a slight smell of sulphur to it.\n")
    time.sleep(2)
    print("Suddenly a laughter erupts, filling the hall and echoing with a menace that shakes your bones.\n")
    time.sleep(2)
    print("\"Hahahah if you're here for the Princess, then your journey has been wasted\".\n")
    time.sleep(2)
    print("At this moment a hulking figure rounds the throne and steps into view.\n")
    time.sleep(2)

def sword_run():
        if weapon=="1":
            print("The sword glistens in your hand, you want to be careful here as you don't want to kill him\n")
            time.sleep(2)
            sword_attack=input("Do you 1) Run and jump at the figure to bring him down or 2) Stand toe to toe with your enemy and give them a chance?\n")
            if sword_attack == "1":
                print("You run at your enemy and with one slash you cut off his arm and he falls to the floor\n")
                time.sleep(2)
                print("You stand over his body\n")
                time.sleep(1.5)
                print("\"where is the Princess?\", You demand\n")
                time.sleep(1.5)
                print("\"You're good with a sword, are you as good with your brain? Answer these riddles and you'll find the Princess\"\n") 
                time.sleep(2.3)
            elif sword_attack=="2":
                print("You and your enemy slowly walk towards each other\n")
                time.sleep(2)
                print("You take a battle stance and swing at your enemy who ducks out of the way and tries to back step\n")
                time.sleep(2)
                print("You are too quick though and slash him with another swing and he falls to the floor\n") 
                time.sleep(2)   
                print("You stand over his body\n")
                time.sleep(1.5)
                print("\"where is the Princess?\", You demand\n")
                time.sleep(1.5)
                print("\"You're good with a sword, are you as good with your brain? Answer these riddles and you'll find the Princess\"\n") 
                time.sleep(2.3)

def riddles():
    print("To save the Princess you must solve the riddles correctly.\n")
    time.sleep(1.5)
    print("One Knight, a Queen, a King, a Princess and a Prince were on a boat.\n")
    time.sleep(2)
    print("The queen, King, Prince and princess fell off the boat. Who was left?\n")
    time.sleep(2)
    riddle_one= input("Who was left? ")
    if riddle_one.lower() == "the knight":
        print("\nYou will not be the Knight in the shining armour by the time I am done with you.\n") 
        riddle_two()   
    elif riddle_one.lower() == "one knight":
        print("\nYou will not be the Knight in the shining armour by the time I am done with you.\n") 
        riddle_two()  
    else:
        print("\nYou have failed to save the princess\n")
        time.sleep(2)
        game_over()     
    
def riddle_two():    
    print("I am not alive, but i grow. I dont have lungs, but I need air.\n")
    time.sleep(2)
    print("I don't have a mouth but water kills me.\n")
    time.sleep(2)
    riddle_two= input("What am I? ")
    if riddle_two.lower() =="fire":
        print("\nYou may think you are getting closer to the princess but this is far from over.\n")
        time.sleep(2)
        riddle_three()
    else:
        print("\nYou have failed to save the princess.\n")
        time.sleep(2)
        game_over()

def riddle_three():    
    print("What has a neck and no head, two arms and no hands?\n")
    time.sleep(2)
    riddle_three=input("What is it? ")
    if riddle_three.lower() =="a top":
      print("\nYou have sucessfully completed the game by saving the princess\n")
      time.sleep(2)
      print(r'''
                                  $""$o
                                $"  $$
                                  $$$$
                                  o "$o
                                o"  "$
            oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$"
""o       o  $          $"       $$$$$       o          $  ooo     o""
    "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
    ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
      "" "$"     """""            ""$"            """      """ "
        $oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
        $$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
          $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$$
          $"""""""""""""""""""""""""""""""""""""""""""""""""""$
          $"                                                  $
          $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$$
''')
    else:
        print("\nYou have failed to save the princess.\n")
        time.sleep(2)
        game_over()

def hammer_run():
    if weapon=="2":
        print("You can feel the weight of the hammer in your hand\n")
        time.sleep(2)
        hammer_attack = input("Do you 1) Use your energy to charge and hope the momentum is enough, or 2) Get the figure to run at you in the hope you can get the perfect hit?\n Type '1' or '2'\n ")
        print(hammer_attack)
        if hammer_attack=="1":
            print("You charge as fast as you can, but the weight throws you off balance and you fall\n")
            time.sleep(2)
            print("You hear the footsteps get closer and everything goes black")
            time.sleep(2)
            game_over()
        elif hammer_attack=="2":
            print("You shout at the laughing figure that he isn't quite big enough to face you\n")
            time.sleep(2)
            print("Suddenly his face goes bright red, he lets out a scream and he charges you\n")
            time.sleep(2)
            print("You ready yourself but as you swing, the figure ducks under your hammer and upper cuts you with such force that your head comes off\n")
            game_over()
        else:
            print("Now now, let's play this properly. Try again.")
            hammer_run()

def magic_wand_run():
    if weapon=="3":
        print("You aren't sure why you picked this weapon but you can now feel the power buzzing at your fingertips\n")
        time.sleep(2)
        print("You don't know how a magic wand works but you know you want to end this fight quickly\n")
        time.sleep(2)
        print("You raise your arm and point the wand at the figure, he goes wide eyed and a light blinds you momentarily\n")
        time.sleep(2)
        print("The light subsides and you see a pair of smoking boots where the figure had been stood\n")
        time.sleep(2)
        print("You feel elated but then the sudden realisation hits you that you don't know where the princess is, you should've kept him alive\n")
        time.sleep(2)
        game_over()

def noweapon_run(): 
    boss_choice = input("What do you do? 1)Shout \"Come at me bro\", or 2) Just run at the hulking figure and hope for the best? \{Type either '1' or '2'\}\n ")
    if boss_choice == "1":
        print("You shout \"Come at me bro\" and the figure laughs again and charges\n")
        time.sleep(2)
        print("You are filled with fear and stay put, without a weapon you can't possibly hope to defend yourself. The figure reaches you and crushes your skull\nwith one mighty swing.\n")
        time.sleep(2.8)
        game_over()
    elif boss_choice == "2":
        print("You set off sprinting at your enemy as fast as you can, your speed makes no substitute for strength and the figure swats you with a wave of his hand. You go crashing into a wall and are splattered.\n")
        time.sleep(2.8)
        game_over()
    else:
        print("Now now, let's play this properly. Try again.")
        noweapon_run()
    
def restart_game_question():
    choice = input("Do you want to play again? Type '1' for Yes or '2' for No: ").lower()
    if choice == "1": 
        print("\nTaking you back\n")
        hero_path()
    elif choice == "2":
        print("\nPfft, loser.")
        time.sleep(2)
    else:
        print("\nSorry, I didn't understand that. Please try again.\n")
        time.sleep(2)
        restart_game_question()    

def ending(current_weapon):
    if(current_weapon == "0"):
        generic_ending()
        noweapon_run()
    if(current_weapon == "1"):
        generic_ending()
        sword_run()
        riddles()
    if(current_weapon == "2"):
        generic_ending()
        hammer_run()
    if(current_weapon == "3"):
        generic_ending()
        magic_wand_run()   

def game_over():
    print(r"""
 @@@@@      @@@@@   @@@   @@ @@@@@@@       @@@@@@  @@   $$ @@@@@@@ @@@@@@
@@         @%   @@ @@@@  @@@ @@         @@     @@ @@    @@ @@     @@   @@
@@    @@@@ @%@@@@@ @@ @@@ @@ @@@@@      @@     @@ @@    @@ @@@@@  @@@@@@
@@     @@  @%   @@ @@  @$ @@ @@         @@     @@  @@  @@  @@     @@   @@
@@@@@@@@   @%   @@ @@     @@ @@@@@@      @@@@@@@    @@@$   @@@@@@ @@   @@

""")
    time.sleep(2)
    print (r"""
                                 ____________ 
                            ,;~'             '~;,
                          ,;                     ;,
                         ;                         ;
                        ,'                         ',
                       ,;                           ;,
                       ; ;      .           .      ; ;
                       | ;   ______       ______   ; |
                       |  `/~"     ~" . "~     "~\'  |
                       |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
                        |   |   $    }:{     $  |   |
                        |   l       / | \       !   |
                        .~  (__,.--" .^. "--.,__)  ~.
                        |     ---;' / | \ `;---     |
                         \__.       \/^\/       .__/
                          V| \                 / |V
                           | |T~\___!___!___/~T| |                  
                           | |`IIII_I_I_I_IIII'| |               
                           |  \,III I I I III,/  |             
                            \   `~~~~~~~~~~'    /               
                              \   .       .   /               
                                \.    ^    ./           
                                  ^~~~^~~~^       
                      
""")
    time.sleep(2)
    restart_game_question()

hero_path()

