# Unique sets of various marks (which can't hold duplicates because they are 
# SET datatype)
cats = {"sphynx", "bengal", "persian"}
cars = {"volvo", "bmw", "mercedes"}
elephants = {"asian", "indian", "african"}
horses = {"arabian", "american", "andalusian"}

# Dicts for various collections as they allow to have name&value pairs.
# Sets inside dicts allows to have editable individual objects that still
# belong to a bigger collections.
collection1 = {"cats": cats, "cars": cars, "elephants": elephants}
collection2 = {"horses": horses, "cars": cars}

# This is a dict that contains other dicts so it's possible to have
# "description" on collections and what they have. 
# Key is used to describe what this collection is
collections = {"catsCarsElephants": collection1, "horsesCars": collection2}


print(collections["catsCarsElephants"]["cats"])

collections["catsCarsElephants"]["cats"].add("britain")

print(collections["catsCarsElephants"]["cats"])