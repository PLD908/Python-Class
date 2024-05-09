# Adventure Game find yourself at a crossroads, with two paths stretching out
question = input("You find yourself at a crossroads, with two paths stretching out before you: one leading into a DARK FOREST and a STEEP MOUNTAIN. Which path will you choose? ")

#  if question is dark forest 
if question.lower() == "dark forest" :

    dark_question = (input("You venture into the dense forest, surrounded by towering trees and the sounds of wildlife. As you walk deeper, you stumble upon an old, abandoned cabin. Do you want to ENTER the cabin, or CONTINUE exploring the forest? "))

    #  if dark forest question is enter 
    if dark_question.lower() == "enter" :
        enter_question = (input("You cautiously approach the cabin and push open the creaky door. Inside, you find a dusty room with a table and chairs. On the table, you see a small wooden chest. Do you want to OPEN the chest, or LEAVE the cabin and explore further? "))

        #  if enter question is open
        if enter_question.lower() == "open" :
            print("You carefully open the chest and discover a small pouch containing valuable gemstones! Congratulations, you've found a hidden treasure in the forest. Your adventure in the dark forest comes to a successful end.")
        #  if enter question is leave
        elif enter_question.lower() == "leave" :
            print("You decide to leave the cabin and continue exploring the forest. As you venture deeper into the woods, you encounter various challenges and mysteries, but ultimately, your adventure in the dark forest comes to an end without discovering the secrets hidden within the cabin.")
        else :
            print("Please enter open or leave")
        
    #  if dark forest question is continue
    elif dark_question.lower() == "continue" :
        continue_question = (input("You press on through the thick underbrush, following a winding path deeper into the forest. Suddenly, you come across a fork in the road, with two diverging paths. One leads deeper into the forest, while the other seems to lead towards a clearing. Do you want to FOLLOW the path into the forest, or HEAD towards the clearing? "))

        #  if continue question is follow
        if continue_question.lower() == "follow" :
            print("You decide to follow the path deeper into the forest, intrigued by the mysteries it may hold. As you journey further, you encounter various challenges and discoveries, navigating through the dense foliage and encountering wildlife along the way. Your adventure leads you through twists and turns until you reach a hidden waterfall cascading into a serene pool. Your exploration of the forest comes to a peaceful end as you soak in the beauty of your surroundings.")
        #  if continue question is head
        elif continue_question.lower() == "head" :
            print("You opt to head towards the clearing, curious about what awaits you beyond the dense forest. As you approach, you find yourself in a tranquil meadow bathed in sunlight, surrounded by colorful wildflowers and chirping birds. The clearing offers a sense of calm and serenity, providing a refreshing break from the dense forest. Your journey through the forest concludes as you bask in the peaceful atmosphere of the clearing, appreciating the beauty of nature.")
        else :
            print("Please enter follow or head")

    else :
        print("Please enter enter or continue")

#  if question is steep mountain
elif question.lower() == "steep mountain":
    steep_question = (input("You begin your ascent up the rugged mountain path, feeling the crisp mountain air and the exhilaration of the climb. As you ascend higher, the terrain becomes increasingly challenging, with steep cliffs and treacherous slopes. Suddenly, you come across a fork in the path, with two diverging routes. One leads towards a narrow ledge overlooking a breathtaking vista, while the other leads into a dark cave. Do you want to CONTINUE towards the ledge, or ENTER the dark cave? "))

    #  if steep question is continue
    if steep_question.lower() == "continue" :
        print("You decide to continue towards the narrow ledge, drawn by the promise of a breathtaking vista. As you cautiously make your way along the rocky path, you are rewarded with a stunning panoramic view of the surrounding landscape. The sight takes your breath away, filling you with a sense of awe and wonder. You spend some time admiring the beauty of the scenery before continuing your journey along the mountain path.")
    #  if steep question is enter
    elif steep_question.lower() == "enter" :
        enter_question = (input("You opt to enter the dark cave, intrigued by the mysteries it may hold within its depths. As you venture deeper into the cavern, the air grows colder and the darkness envelops you. Your footsteps echo off the walls as you navigate through winding passages and stalactite-studded chambers. Suddenly, you come across an ancient chest hidden in a corner of the cave. Do you want to OPEN the chest, or LEAVE the cave and explore further? "))

        #  if enter question is open
        if enter_question == "open" :
            print("You cautiously approach the ancient chest and carefully lift the lid. Inside, you find a collection of priceless artifacts and treasures, shimmering in the dim light of your torch. Your heart races with excitement as you realize the significance of your discovery. Congratulations, you've unearthed a hidden trove of ancient riches! Your adventure in the dark cave comes to a thrilling end.")
        #  if enter question is leave
        elif enter_question == "leave" :
            print("You decide to leave the dark cave and continue exploring the mountain. As you emerge back into the daylight, you feel a sense of relief wash over you. Although you didn't uncover the secrets hidden within the cave, your journey through the mountain has been filled with excitement and adventure. Your exploration of the steep mountain path comes to a close as you continue onwards, eager to discover what other wonders await you in the world.")
        else :
            print("Please enter open or leave")

    else :
        print("Please enter continue or enter")
else :
    print("Please enter dark forest or steep mountain")