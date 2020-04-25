#creating a class
class Things:
    pass

#creating a derived class (from base class)
class Inanimate(Things):
    pass
     
class Animate(Things):
    # example of a class function
    def exist(self):
        print('Cogito ergo sum')

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    # TODO - create three functions for this class: move(), eat(), breathe()
    def move(self):
        print('its_a_run')
        pass
    def eat(self):
        print('is_to_eat')
        pass
    def breathe(self):
        print('recycle_oxygen')
        pass

class Mammals(Animals):
    # TODO - create one function for this class: feed_baby_with_milk()
    def exist(self):
        print('feed_baby_with_milk')
        pass
    pass

class Giraffes(Mammals):
    # TODO - create one function for this class: eat_leaves_from_trees()
    def exist(self):
        print('eat_leaves_from_trees')
        pass
    pass
