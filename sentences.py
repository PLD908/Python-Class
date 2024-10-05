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
        determiners = ["a", "the"]
    else:
        determiners = ["the", "some"]
    return random.choice(determiners)

def starts_with_vowel_sound(word):
    #Check if a word starts with a vowel sound.
    vowel_sounds = ['a', 'e', 'i', 'o', 'u']
    return word[0].lower() in vowel_sounds

class WordBank:
    NOUNS = {
        "living": {
            1: ["student", "teacher", "doctor", "artist", "child", "musician", "writer", "chef", "dancer"],
            2: ["students", "teachers", "doctors", "artists", "children", "musicians", "writers", "chefs", "dancers"]
        },
        "animal": {
            1: ["dog", "cat", "horse", "rabbit", "bird", "puppy", "kitten"],
            2: ["dogs", "cats", "horses", "rabbits", "birds", "puppies", "kittens"]
        },
        "location": ["park", "library", "school", "museum", "café", "garden", "theater", "studio", "bookstore"]
    }
    
    VERBS = {
        "past": ["practiced with", "learned from", "performed for", "read to", "painted with", "photographed"],
        "present": {
            1: ["practices with", "learns from", "performs for", "reads to", "paints with", "photographs"],
            2: ["practice with", "learn from", "perform for", "read to", "paint with", "photograph"]
        },
        "future": ["will practice with", "will learn from", "will perform for", "will read to", "will paint with", "will photograph"]
    }
    
    ADJECTIVES = {
        "personality": ["creative", "curious", "friendly", "helpful", "passionate", "talented", "dedicated"],
        "age": ["young", "experienced"],
        "skill": ["skilled", "expert", "novice", "aspiring"],
        "animal": ["playful", "gentle", "energetic", "quiet", "friendly", "curious"],
        "location": ["quiet", "busy", "popular", "cozy", "elegant", "charming"]
    }
    
    PREPOSITIONS = ["at", "in", "near", "by", "beside"]

def get_unique_word(word_list, used_words):
    #Get a unique word that hasn't been used yet.
    available_words = [word for word in word_list if word not in used_words]
    if not available_words:
        return random.choice(word_list)
    return random.choice(available_words)

def make_sentence(quantity, tense):
    #Build and return a natural, varied sentence.
    used_words = set()
    
    # Subject
    subject_personality = get_unique_word(WordBank.ADJECTIVES["personality"], used_words)
    used_words.add(subject_personality)
    subject_skill = get_unique_word(WordBank.ADJECTIVES["skill"], used_words)
    used_words.add(subject_skill)
    
    subject = get_unique_word(WordBank.NOUNS["living"][quantity], used_words)
    used_words.add(subject)
    
    subject_det = get_determiner(quantity)
    if subject_det == "a" and starts_with_vowel_sound(subject_personality):
        subject_det = "an"
    
    # Verb
    if tense == "present":
        verb = get_unique_word(WordBank.VERBS[tense][quantity], used_words)
    else:
        verb = get_unique_word(WordBank.VERBS[tense], used_words)
    used_words.add(verb)
    
    # Object
    object_category = "animal" if random.random() < 0.7 else "living"
    object_quantity = random.randint(1, 2)
    
    if object_category == "animal":
        object_adj = get_unique_word(WordBank.ADJECTIVES["animal"], used_words)
    else:
        object_adj = get_unique_word(WordBank.ADJECTIVES["personality"], used_words)
    used_words.add(object_adj)
    
    object_noun = get_unique_word(WordBank.NOUNS[object_category][object_quantity], used_words)
    used_words.add(object_noun)
    
    object_det = get_determiner(object_quantity)
    if object_det == "a" and starts_with_vowel_sound(object_adj):
        object_det = "an"
    
    # Location
    location_prep = random.choice(WordBank.PREPOSITIONS)
    location_adj = get_unique_word(WordBank.ADJECTIVES["location"], used_words)
    location = get_unique_word(WordBank.NOUNS["location"], used_words)
    
    location_det = get_determiner(1)
    if location_det == "a" and starts_with_vowel_sound(location_adj):
        location_det = "an"
    
    # Construct the sentence
    subject_phrase = f"{subject_det.capitalize()} {subject_personality}, {subject_skill} {subject}"
    object_phrase = f"{object_det} {object_adj} {object_noun}"
    location_phrase = f"{location_prep} {location_det} {location_adj} {location}"
    
    return f"{subject_phrase} {verb} {object_phrase} {location_phrase}."

def main():
    print("\nGenerated sentences:")
    tenses = ["past", "present", "future"]
    quantities = [1, 2]
    
    for quantity in quantities:
        for tense in tenses:
            print(make_sentence(quantity, tense))

if __name__ == "__main__":
    main()