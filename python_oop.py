#Overview of Classes, Objects, attributes, methods. Inheritance. Subclassing. Overwriting methods. Using super(). 



import turtle #visual library for python


#creating shapes using object oriented programming

#Formula for interior angles of a polygon:
# Sum of interior angle general formula = (n - 2) * 180
# Each angle formula = (n - 2) * 180 / n
# n = sides 

class Polygon: #Capitalize the name of the class

    def __init__(self, sides, name, distance=100, color = "blue", line_thickness = 2):
        self.sides = sides
        self.name = name
        self.distance = distance
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angle = (self.sides - 2 ) * 180
        self.angle = self.interior_angle / self.sides

    def draw_shapes(self): #putting self here will allow us to access the above parameters / attributes. Instead of having to put them all over again
            
        turtle.color(self.color)
        turtle.pensize(self.line_thickness) #pensize is the thicnkess of the lines drawn

        for i in range(self.sides): 
            turtle.forward(self.distance) #() = distance
            turtle.right(180 - self.angle) #() = angle, turning an angle to the right
            #we do 180 - self.angle because self.angle gives the outerior angle of a shape, when we need the interior angle, to get that we do 180 - the outsie angle which is known as taking the supplement


#Note: The self in the above method acts as a connection to the parameters that we described in the main class,
#The function can be written without the self, however then we would need to input all the attributes in the parameter field one by one rather than just typing "Self" to bring them down from above.




#Concept of inheritance and subclassing in OOP: 
# for example: if we need a class for an specific polygon for eg a square, we can utilize the polygonclass above
# as a "parent class" to utilize on the subclass of square. We'll be able to use all of polygon class's attributes this way so we don't have to rewrite it! 

class Square(Polygon):
    def __init__(self, distance=100, color = "blue", line_thickness = 2):
        super().__init__(4, "square", distance, color, line_thickness)
        #super() means take something from the "super" class, or the polygon class
        #using the super() method we were able to get the size, and name, the rest we just put in as we have already utilized on the square's init


 #Method overwriting : useful of subclassing    
 # for eg: if we want to take the draw method and do more with it
 
    def draw_shapes(self):
        turtle.begin_fill()
        super().draw_shapes() #we sorround the actual method with filling 
        turtle.end_fill() 



        
     



#square = Square() #since we created a subclass of polygon already, we don't need to pass in the sides and name, unless we want to overwrite! 



#print(square.draw_shapes())

#turtle.done() #putting this here will keep thie draw window open after it fills in the shape.



#Now we talk about a different class, where we plot points and such 
# we import matplotlib to plot the points

import matplotlib.pyplot as plt



class Point:

    def __init__(self, x, y): #two dimentional points x and y

        self.x = x
        self.y = y

    def __add__(self, other): #other is like a point type, overwiting the add operator

        #this will allow us to print the addition of two points, and addition of point with a integer
        if isinstance(other, Point):
                           
            x = self.x + other.x #addition of two points
            y = self.y + other.y #assuming "other" is another point
            return (Point(x,y))
        else:
            x = self.x + other #addition of a point and an integer
            y = self.y + other
            return(Point(x, y))

    def plot(self):
        plt.scatter(self.x, self.y)  #method to plot points in a graph


point1 = Point(6, 9)
point2 = Point(9, 6)

point3 = point1 + point2
point4 = point1 + 1

#print(point3.x, point3.y)

#print(point4.x, point4.y)

#how to make a third point that is equal to point1 and point2? 
#we can't do point1 + point2 because we get an error sayings unsupported operand type

#concept of operator overloading, we can override the "+" for the point class, making it know how to do the addition although it is not built in
#this idea is executed in the __add__ method, special type in the class

#we can overload other operations as well, like binary, division, <<, >>, etc.