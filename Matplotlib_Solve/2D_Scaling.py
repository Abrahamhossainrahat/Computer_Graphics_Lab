import matplotlib.pyplot as plt

# Step-3 : Calculate the Scaled coordiante
def scale(points, sx, sy):
    scaled = []
    for x, y in points : 
        new_x = x  * sx
        new_y = y * sy
        scaled.append((new_x, new_y))

    return scaled

# Step-1 : Take the points
points = [(1,2), (3,2), (2,4)]

# Step-2 : Take the scaling factor
sx, sy = 2,3

# Call the function 
scaled = scale(points, sx, sy)
print(points)
print(scaled)

# Step-4 : Plot the Original and Scaled 
points += [points[0]]
scaled += [scaled[0]]
# Original 
plt.plot([p[0] for p in points], [p[1] for p in points], marker='s', label = "Original", color='green')
# Scaled
plt.plot([p[0] for p in scaled], [p[1] for p in scaled], marker='s', label = "Scaled", color='red')


plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.legend()
plt.title("2D Scaling")
plt.tight_layout()
plt.show()