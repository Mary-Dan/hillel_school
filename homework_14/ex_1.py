class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or not isinstance(self.c, (int, float)):
            return "Потрібно вводити тільки числа!"
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "З негативними числами нічого не вийде!"
        elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можна побудувати трикутник!"
        else:
            return "Жаль, але з цього трикутник не зробити."
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class ExtTriangle(TriangleChecker, Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

triangle1 = ExtTriangle(3, 4, 5)
print(triangle1.is_triangle())

triangle2 = ExtTriangle(-1, 2, 3)
print(triangle2.is_triangle())

triangle3 = ExtTriangle("a", 2, 3)
print(triangle3.is_triangle())

triangle4 = ExtTriangle(1, 2, 3)
print(triangle4.is_triangle())
