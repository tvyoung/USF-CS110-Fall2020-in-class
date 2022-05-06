#each option has a list of 3 choices that will be picked at random.
import random

people = ["Aly", "Ace", "Moonie"]
places = ["Taiwan", "Canada", "Vietnam"]
adjectives = ["dull", "pleasant", "cool"]
more_adjectives = ["miserable", "horrified", "apathetic"]
plural_nouns = ["chickens", "rambutans", "textbooks"]
more_plural_nouns = ["cakes", "stuffed animals", "gaming consoles"]
diff_places = ["mountains", "metro system", "night market"]
action_verbs = ["skii", "ride trains", "explore"]
more_action_verbs = ["watch films", "play cards", "go snorkeling"]
foods = ["noodles", "salad", "eggs"]
nouns = ["bath house", "valley", "cabin"]

'''Last summer, we went for a vacation with ______ (people) on a trip to _____ (places). The weather there is very ______ (adjectives)! Northern ____ (places) has many ________ (plural_nouns), and they make ____________ (more_plural_nouns) there.

Many people also go to the _________ (diff_places) to _________ (action_verbs). The people that live there love to eat ___________ (foods). They also like to _________ (more_action_verbs) in the sun and swim in the __________ (nouns).'''

#each print line corresponds to different choice/list
print("Last summer, we went for a vacation with " + people[random.randint(0,2)], end='')
print(" on a trip to " + places[random.randint(0,2)] + ".")
print("The weather there is very " + adjectives[random.randint(0,2)] + "!")
print("Northern " + places[random.randint(0,2)], end='')
print(" has many " + plural_nouns[random.randint(0,2)], end='')
print(" and they make " + more_plural_nouns[random.randint(0,2)] + " there.")

print("")

print("Many people also go to the " + diff_places[random.randint(0,2)], end='')
print(" to " + action_verbs[random.randint(0,2)] + ".")
print("The people that live there love to eat " + foods[random.randint(0,2)] + ".")
print("They also like to " + more_action_verbs[random.randint(0,2)], end='')
print(" and swim in the " + nouns[random.randint(0,2)] + ".")


