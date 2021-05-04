
def story():
    template = "Didn't you hear? Supposedly %(noun)s %(verb)s is the new %(color)s."
    dictionary = {}
    dictionary["noun"] = input("Enter a noun: ")
    dictionary["verb"] = input("Enter a -ing verb: ")
    dictionary["color"] = input("Enter a color: ")
    print(template % dictionary)

def story2():
    template = "Every %(period_of_time)s I like to %(verb)s and %(verb2)s my %(emotion)s %(noun)s."
    dictionary = {}
    dictionary["period_of_time"] = input("Enter a length of time: ").lower()
    dictionary["verb"] = input("Enter a verb: ").lower()
    dictionary["verb2"] = input("Enter another verb: ").lower()
    dictionary["emotion"] = input("Enter an emotion: ").lower()
    dictionary["noun"] = input("Enter a noun: ")
    print(template % dictionary)
    
from random import choice
stories = [story, story2]
story_to_run = choice(stories)
story_to_run()
