# Implementação da interface de cor
class Color:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color


#Implementações concretas de cores
class RedColor(Color):
    def __init__(self):
        super().__init__("Red")


class BlueColor(Color):
    def __init__(self):
            super().__init__("Blue")


class GreenColor(Color):
    def __init__(self):
            super().__init__("Green")



# Implementação da interface de forma
class Shape:
    def __init__(self, color):
        self.color = color

    def setColor(self, color):
         self.color = color

    def draw(self):
         raise NotImplementedError("Este método precisa ser implementado pela superclasse")


# Abstrações Refinadas
class CircleShape(Shape):
    def draw(self):
        print(f"Desenhando um circulo {self.color.getColor()}.")

class SquareShape(Shape):
    def draw(self):
        print(f"Desenhando um quadrado {self.color.getColor()}.")

class ShapeFactory:
     def creatShape(self, color):
          raise NotImplementedError("Este método precisa sem implementado pela subclasse")
     
class CircleShapeFactory(ShapeFactory):
     def creatShape(self, color):
          return CircleShape(color)
     
class SquareShapeFactory(ShapeFactory):
     def creatShape(self, color):
          return SquareShape(color)



# Cliente - Utilização do método  ##################
red = RedColor()
blue = BlueColor()
green = GreenColor()

circleShapeFactory = CircleShapeFactory()
squareShapeFactory = SquareShapeFactory()

circle1 = circleShapeFactory.creatShape(red)
circle2 = circleShapeFactory.creatShape(green)
square1 = squareShapeFactory.creatShape(blue)
square2 = squareShapeFactory.creatShape(green)

circle1.draw()
square1.draw()
circle2.draw()
square2.draw()