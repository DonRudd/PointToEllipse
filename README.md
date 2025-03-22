# Orthogonal Projection of a Point onto an ellipse

Given the parametric equation for an ellipse

$$\textbf{x}(t) = \textbf{c} + \textbf{u}\cos{t} + \textbf{v}\sin{t},\ 0 \le t \le 2\pi$$

where x is your position along the elipse given position t, c is the center of the ellipse, u is the vector of representing the length of the major axis, v is the vector representing the length of the minor axis

![image](https://github.com/user-attachments/assets/0e7f6845-d844-4f2a-9b9f-283f0782c1fc)

How do I project a point $\textbf{p}$ onto this parametric equation? We must consider what is going on in this situation. What relationships can we exploit in this situation. When we draw it out, we realize that the line from p to the closest point on your ellipse will be perpendicular to the tangent line at that point (hence the name orthogonal projection). This means that

$$(\textbf{x}(t) - \textbf{p})\cdot \textbf{x}'(t) = 0$$

Expanding this equation out, 

$$\implies (\textbf{c} - \textbf{p} + \textbf{u}\cos{t} + \textbf{v}\sin{t})\cdot (-\textbf{u}\sin{t} + \textbf{v}\cos{t}) = 0$$

$$\implies (c\cdot v - p\cdot v)\cos{t} + (p\cdot u - c\cdot u)\sin{t} + (v^2 - u^2)\cos{t}\sin{t} + (u\cdot v)(\cos^2{t} - \sin^2{t}) = 0$$

Since we assume our axes u and v are orthogonal, $u\cdot v = 0$ and we can get rid of that term. Additionally, using the double angle identity $\sin{2t} = 2\cos{t}\sin{t}$, we can simplify

$$\implies C_1\cos{t} + C_2\sin{t} + C_3\sin{2t} = 0$$

where $C_1 = (\textbf{c} - \textbf{p})\cdot \textbf{v}, C_2 = (\textbf{p} - \textbf{c})\cdot \textbf{u}, C_3 = \frac{1}{2}(\textbf{u}\cdot \textbf{u} - \textbf{v}\cdot \textbf{v})$

How do we solve something like this? Well it can be converted from a trigonometric equation into a polynomial by utilizing [Weierstrass substitution](https://en.wikipedia.org/wiki/Tangent_half-angle_substitution). This involves substituting in $z = \tan\left(\frac{t}{2}\right)$. This substitution comes from the fact that:

[Insert Triangle Graphic Here]

To be continued...

# References:
1. https://math.stackexchange.com/questions/4959431/orthogonal-projection-of-a-point-onto-an-oriented-ellipse-in-r3
2. https://math.stackexchange.com/questions/4513839/find-projection-point-on-elipse
