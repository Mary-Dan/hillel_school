class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        from triangle_check import TriangleChecker

        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or not isinstance(self.c,
                                                                                                          (int, float)):
            return "Сторони повинні бути числами"

        if not TriangleChecker.is_triangle(self.a, self.b, self.c):
            return "Це не є трикутником"

        return "Це є трикутником"

