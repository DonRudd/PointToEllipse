import numpy as np
import matplotlib.pyplot as plt

p = np.array([10, 5])
c = np.array([5, 5])
u = np.array([3, 0])
v = np.array([0, 1.5])

# Defining our objective function f(t)
def f(t):
    vec = c - p + u * np.cos(t) + v * np.sin(t)
    return np.linalg.norm(vec)

# Compute the derivative f'(t) using a central difference approximation.
def f_prime(t, h=1e-5):
    return (f(t + h) - f(t - h)) / (2 * h)

t = 0.1
max_iterations = 1000
tolerance = 1e-6
alpha = 1e-4
beta = 0.8

#Gradient Descent with backtracking line search
for i in range(max_iterations):
    delta_t = -f_prime(t)
    s = 1
    while f(t + s*delta_t) > f(t) - alpha*s*delta_t**2:
        s = beta*s
    t = t + s*delta_t
    if abs(delta_t) <= tolerance:
        print(f'Algorithm ended after {i} iterations.')
        print(f't = {t}, f(t) = {f(t)}')
        break

# Visualization
def ellipse_f(c, u, v, t):
    return c + u * np.cos(t) + v * np.sin(t)

def ellipse_tangent_direction(u, v, t):
    dx_dt = -u[0] * np.sin(t) + v[0] * np.cos(t)
    dy_dt = -u[1] * np.sin(t) + v[1] * np.cos(t)
    len = np.sqrt(dx_dt**2 + dy_dt**2)
    return np.array([dx_dt, dy_dt])/len

def visualize_projection(p, c, u, v):
    closest_point = ellipse_f(c, u, v, t)
    
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
    
    tangent_dir = ellipse_tangent_direction(u, v, t)
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

visualize_projection(p, c, u, v)
