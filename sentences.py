#This program generates English sentences with multiple parts:
#1. A determiner (article)
#2. An adjective (optional)
#3. A noun
#4. A verb
#5. Two prepositional phrases

#The program aims to create more natural-sounding sentences by categorizing words and their relationships.

import random

def get_determiner(quantity):
    #Return a randomly chosen determiner based on the quantity.
    if quantity == 1:
        determiners = ["A", "One", "The"]
    else:
        determiners = ["Some", "Many", "The"]
    return random.choice(determiners)

def get_noun(quantity, type="any"):
    #Return a randomly chosen noun based on quantity and type.
    if quantity == 1:
        if type == "person":
            nouns = ["man", "woman", "child", "teacher", "student", "doctor", "artist"]
        elif type == "animal":
            nouns = ["cat", "dog", "bird", "horse"]
        elif type == "location":
            nouns = ["park", "school", "hospital", "cafe", "library", "office"]
    else:
        if type == "person":
            nouns = ["men", "women", "children", "teachers", "students", "doctors", "artists"]
        elif type == "animal":
            nouns = ["cats", "dogs", "birds", "horses"]
        elif type == "location":
            nouns = ["parks", "schools", "hospitals", "cafes", "libraries", "offices"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    #Return a randomly chosen verb based on quantity and tense.
    if tense == "past":
        verbs = ["walked", "worked", "studied", "visited"]
    elif tense == "present" and quantity == 1:
        verbs = ["walks", "works", "studies", "visits"]
    elif tense == "present" and quantity != 1:
        verbs = ["walk", "work", "study", "visit"]
    elif tense == "future":
        verbs = ["will walk", "will work", "will study", "will visit"]
    return random.choice(verbs)

def get_preposition(type="any"):
    #Return a randomly chosen preposition based on type.
    if type == "location":
        prepositions = ["at", "in"]
    else:  # companion
        prepositions = ["with"]
    return random.choice(prepositions)

def get_adjective(noun_type):
    #Return a randomly chosen adjective appropriate for the noun type.
    if noun_type == "person":
        adjectives = ["friendly", "quiet", "young"]
    else:  # location
        adjectives = ["local", "nearby"]
    return random.choice(adjectives)

def get_prepositional_phrase(type):
    #Build and return a prepositional phrase.
    preposition = get_preposition(type)
    
    if type == "location":
        phrase_quantity = 1
        noun_type = "location"
    else:
        phrase_quantity = random.randint(1, 2)
        noun_type = "person"
    
    determiner = get_determiner(phrase_quantity).lower()
    adjective = get_adjective(noun_type)
    noun = get_noun(phrase_quantity, noun_type)
    
    # Adjust 'a' to 'an' when needed
    if determiner.lower() == "a" and adjective[0].lower() in "aeiou":
        determiner = "an"
    
    return f"{preposition} {determiner} {adjective} {noun}"

def make_sentence(quantity, tense):
    #Build and return a sentence.
    determiner = get_determiner(quantity)
    adjective = get_adjective("person")
    
    # Adjust 'a' to 'an' when needed
    if determiner.lower() == "a" and adjective[0].lower() in "aeiou":
        determiner = "An"
    
    subject = get_noun(quantity, "person")
    verb = get_verb(quantity, tense)
    
    # Always make one phrase about location and one about companions
    location_phrase = get_prepositional_phrase("location")
    companion_phrase = get_prepositional_phrase("companion")
    
    return f"{determiner} {adjective} {subject} {verb} {location_phrase} {companion_phrase}."

def main():
    print("Generated sentences:")
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()