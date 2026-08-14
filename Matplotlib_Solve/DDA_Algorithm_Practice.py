import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    # Take a List
    points = []

    # Step-2 : Calculation dx , dy
    dx = x2 - x1
    dy = y2 - y1

    # Step-3 : Calculate the number of steps
    steps = int(max(abs(dx), abs(dy)))

    # Step-4 : Calculate the increment for x & y
    x_increment = dx/steps
    y_increment = dy/steps

    # Step-5 : Condition and taking all points 
    for i in range(steps+1):
        points.append((round(x1), round(y1)))
        x1 += x_increment
        y1 += y_increment

    return points

# Step-1 : Take Starting and Ending points
x1, y1 = 20, 10
x2, y2 = 30, 18

# Call The Function
points = DDA(x1, y1, x2, y2)

# Print the all points
print("Display all points : ")
print(points)

# Plot the all points 
X = [p[0] for p in points]
Y = [p[1] for p in points]
plt.plot(X, Y, marker = "s")
plt.grid(True)
plt.xlabel("X-Value")
plt.ylabel("Y-Value")
plt.title("Digital Differential Analyzer")
plt.tight_layout()
plt.show()