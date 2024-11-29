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
        c1 = 1e-9
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

p = np.array([0, 5])
c = np.array([5, 5])
u = np.array([3, 0])
v = np.array([0, 1.5])

print(PointToEllipse(p, c, u, v))
visualize_projection(p, c, u, v)
