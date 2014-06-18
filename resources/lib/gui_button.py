import pygame, os, time

class Button:
   os.environ["SDL_FBDEV"] = "/dev/fb1"
   os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
   os.environ["SDL_MOUSEDRV"] = "TSLIB"
   def __init__(self, text):
      self.text = text
      self.is_hover = False
      self.default_color = (255,140,0)
      self.hover_color = (128,0,0)
      self.font_color = (0,0,0)
      self.obj = None
      
   def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_color)
      
   def color(self):
      '''change color when hovering'''
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color
         
   def draw_rect(self, screen, mouse, rectcoord, labelcoord):
      '''create rect obj, draw, and change color based on input'''
      self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
      screen.blit(self.label(), labelcoord)
         
      #change color if mouse over button
      self.check_hover(mouse)
         
   def draw_triangle(self, screen, mouse, trianglecoord, labelcoord):
      self.obj = pygame.draw.polygon(screen, self.color(), trianglecoord)
      self.check_hover(mouse)

   def check_hover(self, mouse):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.obj.collidepoint(mouse):
         self.is_hover = True
      else:
         self.is_hover = False
# End of Class Definition
