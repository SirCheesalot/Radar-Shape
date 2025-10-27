import tkinter as tk
from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class builder:
      def __init__(self, screen):
          self.screen= tk.Frame(screen, width=5000, height=5000) # Embedds the tkinter screen within the simulation class
          self.screen.place(x=100, y= 200)
          # creates the input fields that the user can interact with to form the vertices
          self.vertice1_label= tk.Label(self.screen, text="Vertice 1")
          self.vertice1_label.place(x=10, y=150)
          self.vertice1_var= tk.StringVar()# Spcecial tkinter variable allowing the storage of data entered into entry fields 
          self.vertice1_var.trace_add('write', self.point1)# Uses the trace function in tkinter to call point1 function each time field updated
          self.vertice1 = tk.Entry(self.screen, bd=3, textvariable= self.vertice1_var)
          self.vertice1.place(x=60, y=150)


          self.vertice2_label= tk.Label(self.screen, text="Vertice 2")
          self.vertice2_var= tk.StringVar()
          self.vertice2_var.trace_add('write', self.point2)
          self.vertice2 = tk.Entry(self.screen, bd=3, textvariable= self.vertice2_var)
          self.vertice2_label.place(x=10, y=180)
          self.vertice2.place(x=60, y=180)

          self.vertice3_label= tk.Label(self.screen, text="Vertice 3")
          self.vertice3_var= tk.StringVar()
          self.vertice3_var.trace_add('write', self.point3)
          self.vertice3 = tk.Entry(self.screen, bd=3, textvariable= self.vertice3_var)
          self.vertice3_label.place(x=10, y=210)
          self.vertice3.place(x=60, y=210)

          self.vertice4_label= tk.Label(self.screen, text="Vertice 4")
          self.vertice4_var= tk.StringVar()
          self.vertice4_var.trace_add('write', self.point4)
          self.vertice4 = tk.Entry(self.screen, bd=3,textvariable= self.vertice4_var)
          self.vertice4_label.place(x=10, y=240)
          self.vertice4.place(x=60, y=240)

          self.height_label= tk.Label(self.screen, text="Height")
          self.height_var= tk.StringVar()
          self.height_var.trace_add('write', self.height)
          self.height= tk.Entry(self.screen, bd=3, textvariable= self.height_var)
          self.height_label.place(x=10, y =270 )
          self.height.place(x=60, y=270)

          
          
          

          self.vertex={
                "Vertex1":{"X":12  , "Y":10},
                "Vertex2":{"X":11  , "Y":11},
                "Vertex3":{"X":11  , "Y":12},
                "Vertex4":{"X":12  , "Y":11}}
          self.magnitude= 1


          self.figure= plt.Figure(figsize=(5,4), dpi=100)# generates  the window
          self.ax= self.figure.add_subplot(111, projection='3d')
          self.x= [self.vertex["Vertex1"]["X"], self.vertex["Vertex2"]["X"], self.vertex["Vertex3"]["X"], self.vertex["Vertex4"]["X"] ]
          self.y= [self.vertex["Vertex1"]["Y"], self.vertex["Vertex2"]["Y"], self.vertex["Vertex3"]["Y"], self.vertex["Vertex4"]["Y"]]
          self.z= [0, 0, 0, 0]
          self.ax.scatter(self.x,self.y,self.z)#plots the vertices onto the graph
          self.topface=[[[self.vertex["Vertex1"]["X"],self.vertex["Vertex1"]["Y"], self.magnitude],
                [self.vertex["Vertex2"]["X"],self.vertex["Vertex2"]["Y"], self.magnitude],
                [self.vertex["Vertex3"]["X"],self.vertex["Vertex3"]["Y"], self.magnitude],
                [self.vertex["Vertex4"]["X"],self.vertex["Vertex4"]["Y"], self.magnitude]]]
          self.bottomface=[[[self.vertex["Vertex1"]["X"],self.vertex["Vertex1"]["Y"], 0],
                [self.vertex["Vertex2"]["X"],self.vertex["Vertex2"]["Y"], 0],
                [self.vertex["Vertex3"]["X"],self.vertex["Vertex3"]["Y"], 0],
                [self.vertex["Vertex4"]["X"],self.vertex["Vertex4"]["Y"], 0]]]
          self.sideface1=[[[self.vertex["Vertex1"]["X"], self.vertex["Vertex1"]["Y"], 0],
                            [self.vertex["Vertex2"]["X"], self.vertex["Vertex2"]["Y"], 0],
                            [self.vertex["Vertex2"]["X"], self.vertex["Vertex2"]["Y"], self.magnitude],
                            [self.vertex["Vertex1"]["X"], self.vertex["Vertex1"]["Y"], self.magnitude]]]

          self.sideface2=[[[self.vertex["Vertex2"]["X"], self.vertex["Vertex2"]["Y"], 0],
                          [self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], 0],
                          [self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], self.magnitude],
                          [self.vertex["Vertex2"]["X"], self.vertex["Vertex2"]["Y"], self.magnitude]]]
          self.sideface3=[[[self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], 0],
                         [self.vertex["Vertex4"]["X"], self.vertex["Vertex4"]["Y"], 0],
                         [self.vertex["Vertex4"]["X"], self.vertex["Vertex4"]["Y"], self.magnitude],
                         [self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], self.magnitude]]]

          self.sideface4=[[[self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], 0],
                        [self.vertex["Vertex4"]["X"], self.vertex["Vertex4"]["Y"], 0],
                        [self.vertex["Vertex4"]["X"], self.vertex["Vertex4"]["Y"], self.magnitude],
                        [self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], self.magnitude]]]
          face= self.bottomface+self.topface+self.sideface1+self.sideface2+self.sideface3+self.sideface4
          self.ax.add_collection3d(Poly3DCollection(face))
          
          self.plot= FigureCanvasTkAgg(self.figure, master= self.screen)#Creates the widget within tkinter window for the graph
          self.plot.get_tk_widget().place(x= 240, y= 00)
          self.plot.draw()


      def update_plot(self) :

              self.ax.clear()
              self.x= [self.vertex["Vertex1"]["X"], self.vertex["Vertex2"]["X"], self.vertex["Vertex3"]["X"], self.vertex["Vertex4"]["X"] ]
              self.y= [self.vertex["Vertex1"]["Y"], self.vertex["Vertex2"]["Y"], self.vertex["Vertex3"]["Y"], self.vertex["Vertex4"]["Y"]]
              self.z= self.magnitude
              self.topface=[[[self.vertex["Vertex1"]["X"],self.vertex["Vertex1"]["Y"], self.magnitude], #Creates the faces of the prism
                       [self.vertex["Vertex2"]["X"],self.vertex["Vertex2"]["Y"], self.magnitude],
                       [self.vertex["Vertex3"]["X"],self.vertex["Vertex3"]["Y"], self.magnitude],
                       [self.vertex["Vertex4"]["X"],self.vertex["Vertex4"]["Y"], self.magnitude]]]
 
              self.bottomface=[[[self.vertex["Vertex1"]["X"],self.vertex["Vertex1"]["Y"], 0], 
                         [self.vertex["Vertex2"]["X"],self.vertex["Vertex2"]["Y"], 0],
                         [self.vertex["Vertex3"]["X"],self.vertex["Vertex3"]["Y"], 0],
                         [self.vertex["Vertex4"]["X"],self.vertex["Vertex4"]["Y"], 0]]]

              self.sideface1=[[[self.vertex["Vertex1"]["X"], self.vertex["Vertex1"]["Y"], 0],
                            [self.vertex["Vertex2"]["X"], self.vertex["Vertex2"]["Y"], 0],
                            [self.vertex["Vertex2"]["X"], self.vertex["Vertex2"]["Y"], self.magnitude],
                            [self.vertex["Vertex1"]["X"], self.vertex["Vertex1"]["Y"], self.magnitude]]]

              self.sideface2=[[[self.vertex["Vertex2"]["X"], self.vertex["Vertex2"]["Y"], 0],
                          [self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], 0],
                          [self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], self.magnitude],
                          [self.vertex["Vertex2"]["X"], self.vertex["Vertex2"]["Y"], self.magnitude]]]
              self.sideface3=[[[self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], 0],
                         [self.vertex["Vertex4"]["X"], self.vertex["Vertex4"]["Y"], 0],
                         [self.vertex["Vertex4"]["X"], self.vertex["Vertex4"]["Y"], self.magnitude],
                         [self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], self.magnitude]]]

              self.sideface4=[[[self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], 0],
                        [self.vertex["Vertex4"]["X"], self.vertex["Vertex4"]["Y"], 0],
                        [self.vertex["Vertex4"]["X"], self.vertex["Vertex4"]["Y"], self.magnitude],
                        [self.vertex["Vertex3"]["X"], self.vertex["Vertex3"]["Y"], self.magnitude]]]
              
              face= self.bottomface+self.topface+self.sideface1+self.sideface2+self.sideface3+self.sideface4
              self.ax.add_collection3d(Poly3DCollection(face, alpha= 0.6, edgecolor="black"))#finds the 3d vertex and then joins them together with the alpha allowing transparancy for better visualisation
               
              
          
              self.ax.scatter(self.x,self.y,self.z)#plots the vertices onto the graph
              self.plot.draw()

        
                
          
        
                           
          
          

      def point1(self, *args):# function that stores the user inputs and adds vertice to dictonary
          try: # input validation so only numerical methods are accepted.
               float(self.vertice1_var.get())
               self.vertex_point=self.vertice1_var.get()

               self.vertex["Vertex1"]["X"]= float(self.vertex_point[0:int(len(self.vertex_point)/2)]) #split the numerical value into half to form the x and the y coordianetes
               self.vertex["Vertex1"]["Y"]= float(self.vertex_point[int(len(self.vertex_point)/2):len(self.vertex_point)])
               self.update_plot()
             
                               
          except:
                pass
      def point2(self, *args):
          try:
               float(self.vertice2_var.get())
               self.vertex_point=self.vertice2_var.get()
               self.vertex["Vertex2"]["X"]= float(self.vertex_point[0:int(len(self.vertex_point)/2)]) #split the numerical value into half to form the x and the y coordianetes
               self.vertex["Vertex2"]["Y"]= float(self.vertex_point[int(len(self.vertex_point)/2):len(self.vertex_point)])
               self.update_plot()
               
          except:
                pass
      def point3(self, *args):
          try:
               float(self.vertice3_var.get())
               self.vertex_point=self.vertice3_var.get()
               self.vertex["Vertex3"]["X"]= float(self.vertex_point[0:int(len(self.vertex_point)/2)]) #split the numerical value into half to form the x and the y coordianetes
               self.vertex["Vertex3"]["Y"]= float(self.vertex_point[int(len(self.vertex_point)/2):len(self.vertex_point)])
               self.update_plot()
              
          except:
                pass
          
      def point4(self, *args):
          try:
               float(self.vertice4_var.get())
               self.vertex_point=self.vertice4_var.get()
               self.vertex["Vertex4"]["X"]= float(self.vertex_point[0:int(len(self.vertex_point)/2)]) #split the numerical value into half to form the x and the y coordianetes
               self.vertex["Vertex4"]["Y"]= float(self.vertex_point[int(len(self.vertex_point)/2):len(self.vertex_point)])
               self.update_plot()
             
          except:
                pass
          
              
      def height(self, *args):
          try:
             float(self.height_var.get())
             self.magnitude= float(self.height_var.get())
          except:
                pass
             
          
      

          
   
        










