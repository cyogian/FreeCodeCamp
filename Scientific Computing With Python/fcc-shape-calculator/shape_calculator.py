class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    line = f'{self.width * "*"}\n'
    return line * (self.height)
  
  def get_amount_inside(self, shape_object):
    niw = self.width // shape_object.width
    nih = self.height // shape_object.height
    return niw * nih
  
  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)
    self.side = side
  
  def set_side(self, side):
    self.side = side
    self.width = side
    self.height = side
  
  def set_width(self, width):
    self.set_side(width)
  
  def set_height(self, height):
    self.set_side(height)

  def get_side(self):
    return self.side

  def __str__(self):
    return f'Square(side={self.side})'  