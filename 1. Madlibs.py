#!/usr/bin/env python
# coding: utf-8

# In[1]:


def madlibs():

    story = "Once upon a time, in a {}, there lived a {}. This {} loved to {} every {}. One day, the {} found a {} and decided to {} it."

    # Ask user for input
    place = input("place: ")
    noun = input("noun: ")
    verb = input("verb: ")
    time_unit = input("unit of time: ")
    activity = input("verb ending in -ing: ")
    object_name = input("object: ")
    action_verb = input("action verb: ")

    
    filled_story = story.format(place, noun, verb, time_unit, activity, verb , noun, object_name, action_verb)

    # Display the final story
    print("\nHere's your Madlibs story:\n")
    print(filled_story)


madlibs()


# In[ ]:




