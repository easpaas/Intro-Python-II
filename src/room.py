# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
    return(f"<Room '{self.name}', '{self.description}'>")

  def get_name(self):
    return self.name

  def get_description(self):
    return self.description

  def n_to(self):
    # point to 
    pass

  def s_to(self):
    # points to 
    pass

  def e_to(self):
    # points to
    pass

  def w_to(self):
    # points to
    pass

