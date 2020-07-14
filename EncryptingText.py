import sympy
import random
solved = []
text = input("text: ")
for char in text:
    number = ord(char.lower())
    solved.append(number)
x = sympy.symbols('x')
random_numbers=[]
for i in range(len(solved)):
    r=random.randint(1,100)
    if r not in random_numbers: random_numbers.append(r)
z = x - x
o = z + 1
def linterpolation(y, xs=None):
    if xs is None:
        xs = list(range(1, len(y) + 1))
    assert len(y) == len(xs)

    result = z
    for j, (xj, yj) in enumerate(zip(xs, y)):
        polynomial = o
        for m, xm in enumerate(xs):
            if m != j:
                polynomial *= (x - xm) / (xj - xm)
        result += yj * polynomial
    return sympy.expand(result).evalf()
print(random_numbers)
print(linterpolation(solved, random_numbers ))