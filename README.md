# Orthogonal Projection of a Point onto an ellipse

Given the parametric equation for an ellipse

$$\textbf{x}(t) = \textbf{c} + \textbf{u}\cos{t} + \textbf{v}\sin{t},\ 0 \le t \le 2\pi$$

where x is your position along the elipse given position t, c is the center of the ellipse, u is the vector of representing the length of the major axis, v is the vector representing the length of the minor axis

![image](https://github.com/user-attachments/assets/7898f859-6bf1-44de-bbe7-69b6a730e96c)

How do I project a point $\textbf{p}$ onto this parametric equation? If you agree that the projection of your point onto the ellipse lies along the line from the point to the center, then you must consider what relationships we can exploit in order to create an equation that we can use to solve for t in this situation. You'll notice that the derivative should visually be perpendicular to this line, hence the name orthogonal projection. Using this fact:

$$(\textbf{x}(t) - \textbf{p})\cdot \textbf{x}'(t) = 0 \implies (\textbf{c} - \textbf{p} + \textbf{u}\cos{t} + \textbf{v}\sin{t})\cdot (-\textbf{u}\sin{t} + \textbf{v}\cos{t}) = (-(\textbf{c}\cdot \textbf{u})\sin{t} + (\textbf{c}\cdot \textbf{p})\sin{t})$$

To be continued...

# References:
1. https://math.stackexchange.com/questions/4959431/orthogonal-projection-of-a-point-onto-an-oriented-ellipse-in-r3
2. https://math.stackexchange.com/questions/4513839/find-projection-point-on-elipse
