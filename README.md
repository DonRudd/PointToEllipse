# Orthogonal Projection of a Point onto an ellipse
Two different methods are detailed here
1. [Analytic Method using Weierstrass Substitution](#1-analytic-method-using-weierstrass-substitution)
2. [Iterative Method using Gradient Descent](#2-iterative-method-using-gradient-descent)

---
### 1. Analytic Method using Weierstrass Substitution
Given the parametric equation for an ellipse

$$\textbf{x}(t) = \textbf{c} + \textbf{u}\cos{t} + \textbf{v}\sin{t},\ 0 \le t \le 2\pi$$

where x is your position along the elipse given parameter t, c is the center of the ellipse, u is the vector of representing the length of the major axis, v is the vector representing the length of the minor axis

![image](https://github.com/user-attachments/assets/0e7f6845-d844-4f2a-9b9f-283f0782c1fc)

How do I project a point $\textbf{p}$ onto this parametric equation? We must consider what is going on in this situation. What relationships can we exploit to solve for t? When we draw it out as in the diagram above, we realize that the line from p to the closest point on your ellipse will be perpendicular to the tangent line at that point (hence the name orthogonal projection). This means that

$$(\textbf{x}(t) - \textbf{p})\cdot \textbf{x}'(t) = 0$$

Expanding this equation out, 

$$\implies (\textbf{c} - \textbf{p} + \textbf{u}\cos{t} + \textbf{v}\sin{t})\cdot (-\textbf{u}\sin{t} + \textbf{v}\cos{t}) = 0$$

$$\implies (\mathbf{c}\cdot \mathbf{v} - \mathbf{p}\cdot \mathbf{v})\cos{t} + (\mathbf{p}\cdot \mathbf{u} - \mathbf{c}\cdot \mathbf{u})\sin{t} + (\mathbf{v}\cdot \mathbf{v} - \mathbf{u}\cdot \mathbf{u})\cos{t}\sin{t} + (\mathbf{u}\cdot \mathbf{v})(\cos^2{t} - \sin^2{t}) = 0$$

Since we assume our axes u and v are orthogonal, $u\cdot v = 0$ and we can get rid of that term. Additionally, using the double angle identity $\sin{2t} = 2\cos{t}\sin{t}$, we can simplify

$$\implies C_1\cos{t} + C_2\sin{t} + C_3\sin{2t} = 0$$

where $C_1 = (\textbf{c} - \textbf{p})\cdot \textbf{v}, C_2 = (\textbf{p} - \textbf{c})\cdot \textbf{u}, C_3 = \frac{1}{2}(\textbf{u}\cdot \textbf{u} - \textbf{v}\cdot \textbf{v})$

How do we solve something like this? Well it can be converted from a trigonometric equation into a polynomial by utilizing [Weierstrass substitution](https://en.wikipedia.org/wiki/Tangent_half-angle_substitution). This involves substituting in $z = \tan\left(\frac{t}{2}\right)$. This substitution comes from the fact that:

![image](https://github.com/user-attachments/assets/ed46e52a-956c-4216-8bd3-d4ed7889d8b3)

From this we can derive

$$\sin\left(\frac{t}{2}\right) = \frac{z}{\sqrt{1+z^2}}, \cos\left(\frac{t}{2}\right) = \frac{1}{\sqrt{1+z^2}} \implies \sin{t} = 2\sin\left(\frac{t}{2}\right)\cos\left(\frac{t}{2}\right) = \frac{2z}{1+z^2}, \cos{t} = \cos^2\left(\frac{t}{2}\right) - \sin^2\left(\frac{t}{2}\right) = \frac{1 - z^2}{1 + z^2}, \sin{2t} = \frac{4z(1-z^2)}{(1+z^2)^2}$$

Plugging this into our earlier equation gives us

$$C_1\cos{t} + C_2\sin{t} + C_3\sin{2t} = 0\implies C_1\frac{1-z^2}{1+z^2} + C_2\frac{2z}{1+z^2} + C_3\frac{4z(1-z^2)}{(1+z^2)^2} = 0\implies C_1(1-z^2)(1+z^2) + C_2(2z)(1+z^2) + C_3(4z)(1-z^2) = 0$$

$$-C_1z^4 + (2C_2 - 4C_3)z^3 + (2C_2 + 4C_3)z + C_1 = 0$$

This Polynomial can be solved using any **polynomial/quartic solver** for z. Once you have your roots, for those that are real, solve for t by $t = 2\tan^{-1}(z)$, and identify the closest among them.

# References:
1. https://math.stackexchange.com/questions/4959431/orthogonal-projection-of-a-point-onto-an-oriented-ellipse-in-r3
2. https://math.stackexchange.com/questions/4513839/find-projection-point-on-elipse

---
### 2. Iterative Method using Gradient Descent

Gradient Descent minimizes an objective function $f: \mathbb{R}^n \to \mathbb{R}$. In our case, we want to minimize the distance from a point $\mathbf{p}$ to our ellipse. We can write this as the following: $$\mathbf{x}(t) = \mathbf{c} + \mathbf{u}\cos(t) + \mathbf{v}\sin(t) \\ f(t) = ||\mathbf{x}(t) - \mathbf{p}||_2 = ||\mathbf{c} - \mathbf{p} + \mathbf{u}\cos(t) + \mathbf{v}\sin(t)||_2$$

To be continued...

# References:
1. [Convex Optimization by Stephen Boyd](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
