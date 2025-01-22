import random
choice=["Rock","Paper","Scissor"]
comp=random.choice(choice)
comp_score=0
player_score=0
while True:
    player=input("enter ur choice").capitalize()
    if player==comp:
        print("tie")
        player_score+=1
        comp_score+=1
    elif player=="Rock":
         if comp=="Scissor":
            print("player wins")
            player_score+=1
         else:
            print("comp wins")
            comp_score+=1
    elif player=="Scissor":
        if comp=="Rock":
            print("comp wins")
            comp_score+=1
        else:
            print("player wins")
            player_score+=1
    elif player=="Paper":
        if comp=="Sicssor":
            print("comp wins")
            comp_score+=1
        else:
            print("player wins")
            player_score+=1

    elif player=="End":
        print("final scores")
        print("player_score",player_score)
        print("comp_score",comp_score)
        break

