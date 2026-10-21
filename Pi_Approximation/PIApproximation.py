#PIApproximation.py



"""This program will get an error tolerance number and will approximate
PI closer than the error tolerance number."""


error = float(input("Enter error tolerance:"))

PI = 3.14159265358979
terms = 1

pi_approx = 0

error_calc = 1
print("Number of Terms \t Pi Approximation")
while error_calc > error:
    pi_approx = pi_approx + (4 * ((-1) ** (terms + 1))) / (2 * terms - 1)
    print(terms, "\t", "\t", "\t", "\t", "\t", pi_approx)
    terms += 1
    error_calc = abs(PI - pi_approx)
print(f"After {terms - 1} terms, pi is approximately {pi_approx}. Our error is {error_calc} which is less than or equal to {error}.")
