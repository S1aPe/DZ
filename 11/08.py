from abc import ABC, abstractmethod
import math

# 1. Абстрактный класс Shape
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Возвращает площадь фигуры"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Возвращает периметр фигуры"""
        pass
    
    def description(self):
        """Возвращает описание фигуры"""
        return "Это геометрическая фигура"

# 2. Класс Circle (наследуется от Shape)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Вычисляет площадь круга по формуле π * r²"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Вычисляет длину окружности по формуле 2 * π * r"""
        return 2 * math.pi * self.radius
    
    def description(self):
        return f"Круг с радиусом {self.radius}"

# 3. Класс Rectangle (наследуется от Shape)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Вычисляет площадь как width * height"""
        return self.width * self.height
    
    def perimeter(self):
        """Вычисляет периметр как 2 * (width + height)"""
        return 2 * (self.width + self.height)
    
    def description(self):
        return f"Прямоугольник {self.width}x{self.height}"

# 4. Демонстрация
if __name__ == "__main__":
    # Создаем экземпляры
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    # Тестируем Circle
    print("=== КРУГ ===")
    print(f"Описание: {circle.description()}")
    print(f"Площадь: {circle.area():.2f}")
    print(f"Периметр: {circle.perimeter():.2f}")
    print(f"Базовое описание: {super(Circle, circle).description()}")
    
    print("\n=== ПРЯМОУГОЛЬНИК ===")
    # Тестируем Rectangle
    print(f"Описание: {rectangle.description()}")
    print(f"Площадь: {rectangle.area()}")
    print(f"Периметр: {rectangle.perimeter()}")
    print(f"Базовое описание: {super(Rectangle, rectangle).description()}")
    
    # Дополнительная демонстрация с полиморфизмом
    print("\n=== ПОЛИМОРФИЗМ ===")
    shapes = [circle, rectangle]
    
    for shape in shapes:
        print(f"\n{shape.description()}")
        print(f"Площадь: {shape.area():.2f}")
        print(f"Периметр: {shape.perimeter():.2f}")