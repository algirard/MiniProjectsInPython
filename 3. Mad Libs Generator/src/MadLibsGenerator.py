
def story():
    template = "Didn't you hear? Supposedly %(noun)s %(verb)s is the new %(color)s."
    dictionary = {}
    dictionary["noun"] = raw_input("Enter a noun: ")
    dictionary["verb"] = raw_input("Enter a -ing verb: ")
    dictionary["color"] = raw_input("Enter a color: ")
    print template % dictionary

def story2():
    template = "Every %(period_of_time)s I like to %(verb)s and %(verb2)s my %(emotion)s %(noun)s."
    dictionary = {}
    dictionary["period_of_time"] = raw_input("Enter a length of time: ").lower()
    dictionary["verb"] = raw_input("Enter a verb: ").lower()
    dictionary["verb2"] = raw_input("Enter another verb: ").lower()
    dictionary["emotion"] = raw_input("Enter an emotion: ").lower()
    dictionary["noun"] = raw_input("Enter a noun: ")
    print template % dictionary
    
from random import choice
stories = [story, story2]
story_to_run = choice(stories)
story_to_run()
