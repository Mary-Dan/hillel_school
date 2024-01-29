from triangle import Triangle
from user_input import get_user_input

triangle1 = Triangle(3, 4, 5)
print(triangle1.is_triangle())

triangle2 = Triangle(-1, 2, 3)
print(triangle2.is_triangle())

triangle3 = Triangle("a", 2, 3)
print(triangle3.is_triangle())

triangle4 = Triangle(1, 2, 3)
print(triangle4.is_triangle())

result = get_user_input()
print(f"Результат введення користувача: {result}")
