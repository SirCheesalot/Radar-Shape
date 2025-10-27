import tkinter as tk
from Shapebuilder import builder
from Radar import model

class simulation:

      def __init__(self):
          self.screen= tk.Tk()
          self.object = builder(self.screen)
          self.screen.geometry('1000x1000')
          self.a_label= tk.Label(self.screen, text="Altitude")#Label to help navigate the parameters by naming them
          self.a_label.place(x=300, y=300)
          self.radar= model(self.object, 5)
          print(self.radar.ray_intersection())

       
        

      def run(self):
          self.screen.mainloop()

sim= simulation()
sim.run()
