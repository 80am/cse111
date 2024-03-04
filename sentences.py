#added a second prepositional phrase that is different from the first
#I also added a get_adjective function and called it in the make_sentence function


import random

# Create a list of strings and assign
# the list to a variable named words.
#words = ["boy", "girl", "cat", "dog", "bird", "house"]

# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
#word = random.choice(words)

def main():
    #a.	single	past
    #b.	single	present
    #c.	single	future
    #d.	plural	past
    #e.	plural	present
    #f.	plural	future


    print(make_sentence(1, 'past'))
    print(make_sentence(1, 'present'))
    print(make_sentence(1, 'future'))
    print(make_sentence(2, 'past'))
    print(make_sentence(2, 'present'))
    print(make_sentence(2, 'future'))

    pass

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        noun_words = ["bird", "boy", "car","cat", "child", "dog", "girl", "man","rabbit","woman"]
    else:
        noun_words = ["birds", "boys", "cars","cats", "children", "dogs", "girls", "men","rabbits","women"]

    # Randomly choose and return a determiner.
    noun_word = random.choice(noun_words)
    return noun_word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past':
        tense_words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        tense_words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present' and quantity != 1:
        tense_words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        tense_words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]


    verb_word = random.choice(tense_words)
    return verb_word

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    amount = quantity
    the_tense = tense
    

    deter = get_determiner(amount)
    nouner = get_noun(amount)
    verber = get_verb(amount, the_tense)
    #prepo = get_preposition()
    prepo_phrase = get_prepositional_phrase(amount)
    prepo_phrase2 = get_prepositional_phrase(amount)
    adjective = get_adjective()

    return(f'And the sentence goes like:{deter.capitalize()} {adjective} {nouner} {verber} {prepo_phrase} {prepo_phrase2}.' )


def get_preposition():
        """Return a randomly chosen preposition
        from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
        preposition_words = ["about", "above", "across", "after",  \
         "along","around", "at", "before", "behind", "below",\
             "beyond", "by", "despite", "except", "for","from",\
                  "in", "into", "near", "of","off", "on", "onto",\
                       "out", "over","past", "to", "under", "with", "without"]
        preposition_word = random.choice(preposition_words)

        return preposition_word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    amount = quantity
    phrase = f'{get_preposition()} {get_determiner(amount)} {get_noun(amount)}'

    return phrase

def get_adjective():
    adjective_list = ['ashamed', 'adorable', 'attractive', 'beautiful', 'awful', 'aggressive', 'cruel', 'clever', 'tasty', 'jealous']

    adjective_word = random.choice(adjective_list)

    return adjective_word

main()