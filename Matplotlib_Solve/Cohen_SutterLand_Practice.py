import matplotlib.pyplot as plt

# Step-1 : Assignb all side 
inside = 0
left = 1
right = 2
top = 8
bottom = 4

# Step-3 : Generate Outcode for (x1,y1) & (x2,y2)
def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = inside 
    if x < xmin :
        code |= left
    if x > xmax :
        code |= right
    if y < ymin : 
        code |= bottom
    if y > ymax : 
        code |= top

    return code


# Step-4 : Clipping candidate and clip the line

def cohen_sutterland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):

    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    m = (y2-y1)/ (x2-x1)
    accept = False
    while True : 
        if not (code1 | code2) : 
            accept = True
            break
        elif code1 & code2 :
            break
        else :
            code_out = code1 if code1 != 0 else code2

            if code_out & top :
                x = x1 + (ymax - y1)/m
                y = ymax
            elif code_out & bottom :
                x = x1 + (ymin - y1)/m
                y = ymin
            elif code_out & right : 
                x = xmax
                y = y1 + (xmax - x1)*m
            elif code_out & left : 
                x = xmin
                y = y1 + (xmin - x1)*m
            
            if code_out == code1 :
                x1 , y1 = x, y
                code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
            else : 
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    if accept : 
        return x1, y1, x2, y2
    return None


# Step-2: Take window and line 
# Window
xmin, ymin = 2, 2
xmax, ymax = 8, 7

# Line
origin = (0, 3, 10, 8)  # x1, y1, x2, y2

# Call The fucntion 
result = cohen_sutterland(*origin, xmin, ymin, xmax, ymax)

print(result)

# Plot the window
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin])

# Plot the original line
plt.plot([origin[0], origin[2]], [origin[1], origin[3]], linestyle = '--')

# Plot the sutterland line
plt.plot([result[0], result[2]], [result[1], result[3]], linewidth = 3)

plt.grid(True)
plt.title("Cohen Sutterland Line Clipping Algorithm")
plt.tight_layout()

plt.show()