import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def PointToEllipse(p, c, u, v):
    # Orthogonal Projection Obtained by solving (x(t) - p).x'(t) = 0 and using Weierstrass Substitution
    c1 = np.dot(c - p, v)
    c2 = np.dot(p - c, u)
    c3 = 0.5 * (np.dot(v, v) - np.dot(u, u))
    if c1 == 0 and c2 < 0:
        # Odd things happen when your point is in line with the major axis on the negative side? [1, 5]
        # I'm guessing because the polynomial reduces to x^3 + x = 0 --> x(x^2 + 1) = 0 and this has ONE real solution.
        c1 = 1e-4
    roots = Polynomial([c1, 2*c2 + 4*c3, 0, 2*c2 - 4*c3, -c1]).roots()
    closest = None
    for z in roots:
        if z.imag == 0: # Only want real solutions
            t = 2*np.atan(z.real)
            pt = c + u*np.cos(t) + v*np.sin(t)
            print(pt)
            if closest is None or np.linalg.norm(pt - p) < np.linalg.norm(closest - p):
                #or acts like an if-elseif (behaves sequentially), so it'll check statement 1 THEN statement 2 if it's false.
                closest = pt
    return closest

print(PointToEllipse(np.array([0, 5]), np.array([5, 5]), np.array([3, 0]), np.array([0, 1.5])))
#print(PointToEllipse(np.array([10, 5]), np.array([5, 5]), np.array([3, 0]), np.array([0, 1.5])))

'''
Cubic and Quartic Reference: https://quarticequations.com/Tutorial.pdf
Project Point onto Ellipse
	References:
		1. https://math.stackexchange.com/questions/4959431/orthogonal-projection-of-a-point-onto-an-oriented-ellipse-in-r3
		2. https://math.stackexchange.com/questions/4513839/find-projection-point-on-elipse

My Cubic & Quartic Solver:
def solveCubic(a, b, c, d): # ax^3 + bx^2 + cx + d = 0 --> to std form --> x^3 + (b/a)x^2 + (c/a)x + (d/a) = 0
    #z^3 + a2*z^2 + a1*z + a_0 = 0
    b, c, d = b/a, c/a, d/a
    q = c/3 - b**2/9
    r = (c*b - 3*d)/6 - b**3/27
    discr = r**2 + q**3
    if discr > 0: # Only one real solution
        A = (abs(r) + np.sqrt(discr))**(1/3)
        t1 = A - q/A if r >= 0 else q/A - A
        z1 = t1 - b/3  # z1 is the only guaranteed real solution, z2 = x2 + iy2, z3 = x3 + iy3
        x2 = -t1/2 - b/3
        x3 = x2
        y2 = np.sqrt(3)/2 * (A + q/A)
        y3 = -y2
        if y2 != 0 and y3 != 0:
            return z1, float("nan")
        elif y2 != 0 and y3 == 0:
            return z1, x3
        elif y3 != 0 and y2 == 0:
            return z1, x2
    elif discr <= 0: # Three real solutions
        theta = None
        if q == 0:
            theta = 0
        elif q < 0:
            theta = np.acos(r/(-q)**(3/2))
        phi1 = theta/3
        phi2 = phi1 - 2*np.pi/3
        phi3 = phi1 + 2*np.pi/3
        rootq, b3 = 2*np.sqrt(-q), b/3
        z1 = rootq*np.cos(phi1) - b3
        z2 = rootq*np.cos(phi2) - b3
        z3 = rootq*np.cos(phi3) - b3
        return z1, z2, z3

def solveQuartic(a, b, c, d, e):
    if a == 0:
        return solveCubic(b, c, d, e)
    else:
        b, c, d, e = b/a, c/a, d/a, e/a
        C = b/4
        b2 = c - 6*C**2
        b1 = d - 2*c*C + 8*C**3
        b0 = e - d*C + c*C**2 - 3*C**4
        #m^3 + b2*m^2 + (b2^2/4 - b_0)*m - b1^2/8 = 0
        m = solveCubic(1, b2, b2**2/4 - b0, -b1**2/8)[0]
        sigma = 1 if b1 > 0 else -1
        R = sigma * np.sqrt(m**2 + b2*m + b2**2/4 - b0)
        discr1, discr2 = -m/2 - b2/2 - R, -m/2 - b2/2 + R
        discr1 = np.sqrt(discr1) if discr1 >= 0 else float("nan")
        discr2 = np.sqrt(discr2) if discr2 >= 0 else float("nan")
        Z1 = np.sqrt(m/2) - C - discr1
        Z2 = np.sqrt(m/2) - C + discr1
        Z3 = -np.sqrt(m/2) - C + discr2
        Z4 = -np.sqrt(m/2) - C - discr2
        return Z1, Z2, Z3, Z4

def PointToEllipse(p, c, u, v):
    # Orthogonal Projection Obtained by solving (x(t) - p).x'(t) = 0 and using Weierstrass Substitution
    c1 = np.dot(c - p, v)
    c2 = np.dot(p - c, u)
    c3 = 0.5 * (np.dot(v, v) - np.dot(u, u))
    if c1 == 0 and c2 < 0:
        # Odd things happen when your point is in line with the major axis on the negative side? [1, 5]
        # I'm guessing because the polynomial reduces to x^3 + x = 0 --> x(x^2 + 1) = 0 and this has ONE real solution.
        c1 = 0.0001
    roots = solveQuartic(-c1, 2*c2 - 4*c3, 0, 2*c2 + 4*c3, c1)
    closest = None
    for z in roots:
        if z == z: # if z ~= z then it's nan, so z == z is not nan.
            t = 2*np.atan(z)
            pt = c + u*np.cos(t) + v*np.sin(t)
            print(pt)
            if (closest is None) or (closest is not None and np.linalg.norm(pt - p) < np.linalg.norm(closest - p)):
                closest = pt
    return closest
'''

'''
# GPT Generated Visualizer
def visualize_projection(p, c, u, v):
    closest_point = PointToEllipse(p, c, u, v)

    # Define the ellipse
    t = np.linspace(0, 2 * np.pi, 100)
    ellipse = c[:, np.newaxis] + u[:, np.newaxis] * np.cos(t) + v[:, np.newaxis] * np.sin(t)

    # Understanding this np.newaxis notation:
    # 1. https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis
    # 2. https://www.reddit.com/r/learnpython/comments/13vs2fu/need_help_to_understand_the_notation_x_npnewaxis/

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.plot(ellipse[0], ellipse[1], label='Ellipse')
    plt.scatter(*p, color='red', label='Point P')
    plt.scatter(*closest_point, color='blue', label='Closest Point on Ellipse')
    plt.plot([p[0], closest_point[0]], [p[1], closest_point[1]], 'k--', label='Projection Line')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Projection of Point onto Ellipse')
    plt.grid(True)
    plt.show()

visualize_projection(np.array([0, 5]), np.array([5, 5]), np.array([3, 0]), np.array([0, 1.5]))
'''
