import matplotlib.pyplot as plt

def bresenham(x1, x2, y1, y2):
    # Take a List
    points = []

    #Step-2 : Calculate dx , dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    #Step-3 : Determine Direction
    Sx = 1 if x1<x2 else -1
    Sy = 1 if y1<y2 else -1
    
    # Step-3 : Take Initial error
    err = dx - dy

    # Dicission Rules
    while True : 
        points.append((x1, y1))
        e2 = 2 * err
        if x1==x2 and y1==y2 :
            break
        
        if e2 > -dy :
            err -= dy
            x1 += Sx
        if e2 < dx :
            err += dx
            y1 += Sy

    return points

#Step-1 : Take Starting and Ending Point
x1, y1 = 20, 10
x2, y2 = 30, 18

# Call the function
points = bresenham(x1, x2, y1, y2)

# Print the points
print("Display All Points : ")
print(points)

# Display the points 
X1 = [p[0] for p in points]
Y1 = [p[1] for p in points]

plt.plot(X1, Y1, marker ='s')
plt.grid(True)
plt.xlabel("X-Value")
plt.ylabel("Y-Value")
plt.title("Bresenham's Line Drawing Algorithm")
plt.show()