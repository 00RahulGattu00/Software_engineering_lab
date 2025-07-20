for i, line in enumerate(open("input2.txt"), 1):
    try:
        a, b, c = map(float, line.split())
        if a == 0: print(f"Line {i}: Not quadratic"); continue
        d = b**2 - 4*a*c
        if d < 0: print(f"Line {i}: No real roots"); continue
        r1 = (-b + d**0.5) / (2*a)
        r2 = (-b - d**0.5) / (2*a)
        print(f"Line {i}: Roots = {r1:.2f}, {r2:.2f}")
    except: print(f"Line {i}: Invalid input")
