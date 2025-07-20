a, b, c = map(float, open("input.txt").read().split())

d = b**2 - 4*a*c

if d < 0:
    print("No real roots")
else:
    r1 = (-b + d**0.5) / (2*a)
    r2 = (-b - d**0.5) / (2*a)
    print("Roots:", r1, "and", r2)
