class Art:
  def __init__(self, artist, title, medium, year):
    self.artist = artist 
    self.title = title 
    self.medium = medium 
    self.year = year
    
  def __repr__(self):
    return "{}. \"{}\". {}, {}".format(self.artist, self.title, self.year, self.medium)

class Marketplace:
  def __init__(self, listings):
    self.listings = listings
  def add_listing(self, new_listing):
    self.listing.append(new_listing)
  def remove_listing(self):
    pass
  def show_listing(self):
    for listing in self.listings:
      print(listing)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas")

print(girl_with_mandolin)

veneer = Marketplace([girl_with_mandolin])
veneer.show_listing()

