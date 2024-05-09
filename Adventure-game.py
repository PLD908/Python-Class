# Adventure Game
question = input("Are you a BOY or a GIRL? ")
if question.lower() == "boy" :
    boy_question = (input("You are a girl, so what is your favorite game? FOOTBALL/BASKETBALL? "))
    if boy_question.lower() == "football" :
        football_question = (input("Who is your favorite player? "))
        if football_question :
            second_football_question = (input("What is your football club? "))
            print(f"Your favorite player is {football_question} and your favorite club is {second_football_question}")
    elif boy_question.lower() == "basketball" :
        basketball_question = (input("Who is your favorite player? "))
        if basketball_question :
            second_basketball_question = (input("What is your football club? "))
            print(f"Your favorite player is {basketball_question} and your favorite club is {second_basketball_question}")
    else :
        print("You are a GIRL")
elif question.lower() == "girl":
    girl_question = (input("You are a girl, so what is your favorite game? FOOTBALL/BASKETBALL? "))
    if girl_question.lower() == "football" :
        football_question = (input("Who is your favorite player? "))
        if football_question :
            second_football_question = (input("What is your football club? "))
            print(f"Your favorite player is {football_question} and your favorite club is {second_football_question}")
    elif girl_question.lower() == "basketball" :
        basketball_question = (input("Who is your favorite player? "))
        if basketball_question :
            second_basketball_question = (input("What is your football club? "))
            print(f"Your favorite player is {basketball_question} and your favorite club is {second_basketball_question}")
    else :
        print("You are a GIRL")
else :
    print("You are neither a BOY nor a GIRL")