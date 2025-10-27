import tkinter as tk
from Simulation import simulation

class Main: #Class that would construct the buttons on the screen
      def __init__(self):
        self.screen= tk.Tk()
        self.screen.title("Radar Simulator")#Parameters for the screen
        self.screen.geometry('350x350')
        self.start_button= tk.Button(self.screen, text="Start", command=self.start)#Creates the buttons needed for the simulation to move onto the different states.
        self.settings_button= tk.Button(self.screen, text="Settings", command=self.settings)
        self.help_button= tk.Button(self.screen, text="Help", command=self.help)
        self.help_button.pack(side= 'bottom')
        self.settings_button.pack(side= 'bottom')
        self.start_button.pack(side= 'bottom')
      
      
        
        

      def start(self): #Function would change the program to the simulation state
          self.screen.destroy() #removes menu screen
          self.simulation_screen = simulation()
          self.simulation_screen.run()

        
      def help(self):
          Help_State= True

      def settings(self):
          Settings_State= True
          
     
      def run(self):
          self.screen.mainloop()  #Creates the main screen where buttons will be then placed
Main()
        

