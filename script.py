class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist 
    self.title = title 
    self.medium = medium 
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return "{}. \"{}\". {}, {}. The owner is {} located in {}".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

class Marketplace:
  def __init__(self, *listings):
    self.listings = listings
  def add_listing(self, new_listing):
    self.listing.append(new_listing)
  def remove_listing(self):
    pass
  def show_listing(self):
    for listing in self.listings:
      print(listing)

class Client:
  def __init__(self, name, is_museum, location = "Private Collection"):
    self.name = name 
    self.location = location
    self.is_museum = is_museum 

veneer = Marketplace([])
veneer.show_listing()

adytta = Client("Edytta Hapirt", False)
moma = Client("The MOMA", True, "New York")

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", adytta)
print(girl_with_mandolin)