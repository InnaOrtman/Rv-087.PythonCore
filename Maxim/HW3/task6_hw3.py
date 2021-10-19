# Task 6*
# 1. Suppose that you are a philatelist. You have three collections of marks.
# The first one contains marks dedicated to cats, the second one holds cars
# and the third one has elephants. You can exchange by your collections with
# another philatelists, but only entire collections (for example, change
# cars on bicycles), but not the single marks.
#
# Also you want to have short description of each collection.
#
# Please suggest the most appropriate way of saving information about collections, marks they consist of and their descriptions.
#
# 2. Suppose you have equal marks in collection  with cats and you want to hold information only about unique ones. How would you save this information?

# 1)
# philatelist = [([("Mark_of_cat_1", value), ], "description of colection_cats"),
#               ([("Mark_of_car_1", value), ], "description of colection_cars"),
#               ([("Mark_of_elephant_1", value), ], "description of colection_elephants")
#               ]

# 2) Uniq colection
# set([("Mark_of_cat_1", value), ])
