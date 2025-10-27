import numpy as np
from Shapebuilder import builder
import random

class model:

      def __init__(self, shape, distance):
          self.shape= shape.vertex
          self.distance = distance
          self.bottomface = shape.bottomface
          self.topface = shape.topface
          self.frontface= shape.sideface1
          self.height= shape.magnitude

          
          self.points = np.array([[self.shape["Vertex1"]["X"],self.shape["Vertex1"]["Y"]],
                                  [self.shape["Vertex2"]["X"],self.shape["Vertex2"]["Y"]],
                                  [self.shape["Vertex3"]["X"],self.shape["Vertex3"]["Y"]],
                                  [self.shape["Vertex4"]["X"],self.shape["Vertex4"]["Y"]]])
          self.centroid = self.points.mean(axis=0)
          #finds the center of the shape created
          self.origin= np.array([self.centroid[0]+self.distance, self.centroid[1], 0])
          #point at which the location of the radar would be so that it is always centered.
          
      def rays(self):
          self.sideangle = random.uniform(0, np.pi) # Creates the angle that the rays would be fired at
          self.elevation = random.uniform(0, np.pi)# Random is used to allow the modeling of radars probability of detectin and object

          self.direction = {"x":np.sin(self.sideangle)*np.cos(self.elevation), "y": np.sin(self.sideangle)*np.sin(self.elevation), "z": np.cos(self.elevation)}#creates the 3d vectors
          self.direction_array = np.array([self.direction["x"], self.direction["y"], self.direction["z"]])

          self.ray= np.array([self.direction_array, self.origin]) # creates ray

          self.reciever= np.array([[self.origin[0]+4, self.origin[1]+4, 0], #coordinates of the box around the reciever that will be checked against the reflection of the ray
                                   [self.origin[0]-4, self.origin[1]+4, 0],
                                   [self.origin[0]+4, self.origin[1]-4, 0],
                                   [self.origin[0]-4, self.origin[1]-4, 0],
                                   [self.origin[0]+4, self.origin[1]+4, 5],
                                   [self.origin[0]-4, self.origin[1]+4, 5],
                                   [self.origin[0]+4, self.origin[1]-4, 5],
                                   [self.origin[0]-4, self.origin[1]-4, 5]])

       
          
       

      def ray_intersection(self): #Checks if the ray intersects with the prism
          self.hit=0 #number of times the radar has hit the prism

          for i in range(250):
            self.rays()
            self.travel= np.zeros((1, 4))
            self.intersected= np.full((1, 4), True)

            self.pvec= np.cross(self.ray[0], self.bottomface) #Checks if the ray is in parrallel with the plane of the bottom face
            self.det = np.sum(self.topface*self.pvec, axis=2)# Sees if it's in parallel with the plane of the topface to fully check if it would never intersect prism
            self.non_intersecting_indicies = np.absolute(self.det) < 0.000001

            self.travel[self.non_intersecting_indicies]=np.nan
            self.intersected[self.non_intersecting_indicies] = False #Checks if it intersects with the front face

            self.inv_det = 1.0/self.det
            self.tvec= self.ray[1]-self.frontface
            self.ray_translation = np.sum(self.tvec*self.pvec, axis=2)*self.inv_det       

            self.non_intersecting_indicies= (self.ray_translation < 0.0)+(self.ray_translation >1.0)
            self.travel[self.non_intersecting_indicies]=np.nan
            self.intersected[self.non_intersecting_indicies]= False
            self.qvec= np.cross(self.tvec, self.frontface)
            self.edge = np.sum(self.ray[0]*self.qvec, axis=2)*self.inv_det
            
            

            

            self.travel[self.non_intersecting_indicies]=np.nan
            self.intersected[self.non_intersecting_indicies]= False
            
      
            
           
            

            if np.all((self.det)> 0.000001):
      
               self.front= np.array(self.frontface[0])

               self.edge1= self.front[1]-self.front[0]
               self.edge2= self.front[3]-self.front[0]
               self.front_vector= np.cross(self.edge1, self.edge2)#Finds the cross product so the vector is moving horizontaly to the vertical front face
               self.reflection = self.ray[0]-2*(np.dot(self.ray[0], self.front_vector))*self.front_vector
               print("initial",self.ray[0],"reflection", self.reflection)
               self.return_pvec= np.cross(self.reflection, self.reciever) #calculates if the ray is parallel to the box around the origin
               self.return_det = np.sum(self.reciever*self.return_pvec, axis=1)
               self.return_non_intersecting = np.absolute(self.det)< 0.00001
               if np.any(np.absolute(self.return_det))> 0.000001:
                  self.hit += 1
                  print("hits", self.hit)
               
               
               
               
         
      
        
            
            
      

      
