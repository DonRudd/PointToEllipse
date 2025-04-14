import numpy as np 
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def PointToEllipse(p, c, u, v): # Orthogonal Projection Obtained by solving (x(t) - p).x'(t) = 0 and using Weierstrass Substitution
    c1 = np.dot(c - p, v)
    c2 = np.dot(p - c, u)
    c3 = 0.5 * (np.dot(v, v) - np.dot(u, u))
    if c1 == 0 and c2 < 0:
        c1 = 1e-9
    roots = Polynomial([c1, 2*c2 + 4*c3, 0, 2*c2 - 4*c3, -c1]).roots()
    closest = None
    best_t = None
    for z in roots:
        if z.imag == 0:
            t = 2*np.atan(z.real)
            pt = c + u*np.cos(t) + v*np.sin(t)
            if closest is None or np.linalg.norm(pt - p) < np.linalg.norm(closest - p):
                closest = pt
                best_t = t
    return closest, best_t

def ellipse_tangent_direction(c, u, v, t):
    dx_dt = -u[0] * np.sin(t) + v[0] * np.cos(t)
    dy_dt = -u[1] * np.sin(t) + v[1] * np.cos(t)
    return np.array([dx_dt, dy_dt])

def visualize_projection(p, c, u, v):
    closest_point, t = PointToEllipse(p, c, u, v)
    
    t_vals = np.linspace(0, 2 * np.pi, 100)
    ellipse = c[:, np.newaxis] + u[:, np.newaxis] * np.cos(t_vals) + v[:, np.newaxis] * np.sin(t_vals)
    # Converted c, u, v shapes from (2,) to (2,1) in order for matrix multiplication to take place with t which is (1,100) in this case. It'll show up as (100,) as all vectors do
    
    plt.figure(figsize=(6, 6))
    plt.plot(ellipse[0], ellipse[1], label='Ellipse')
    plt.plot([p[0], closest_point[0]], [p[1], closest_point[1]], 'k-', zorder=0) # Projection Line

    AxisPos1 = c + u
    AxisPos2 = c + v

    plt.plot([c[0], AxisPos1[0]], [c[1], AxisPos1[1]], 'k-', zorder=0)
    plt.plot([c[0], AxisPos2[0]], [c[1], AxisPos2[1]], 'k-', zorder=0)
    plt.scatter(*p, color='red', label='Point P')
    plt.scatter(*closest_point, color='blue', label='Closest Point on Ellipse')
    plt.scatter(*c, color=(0, 255/255, 156/255), label='Center')
    plt.scatter(*AxisPos1, color='purple')
    plt.scatter(*AxisPos2, color='purple')
    
    tangent_dir = ellipse_tangent_direction(c, u, v, t)
    tangent_dir /= np.linalg.norm(tangent_dir)  # Normalize direction vector
    scale = 2  # Scale factor for better visibility
    tangent_start = closest_point - scale * tangent_dir
    tangent_end = closest_point + scale * tangent_dir
    plt.plot([tangent_start[0], tangent_end[0]], [tangent_start[1], tangent_end[1]], 'g-', label='Tangent Line at Closest Point')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Projection of Point onto Ellipse with Tangent Line')
    plt.grid(True)
    plt.show()

p = np.array([7, 2])
c = np.array([5, 5])
u = np.array([3, 0])
v = np.array([0, 1.5])

visualize_projection(p, c, u, v)
