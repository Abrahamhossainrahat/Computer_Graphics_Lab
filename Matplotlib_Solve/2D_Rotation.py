import matplotlib.pyplot as plt
import math

# Step-3 : Calculate the rotation
def rotate(points, theta):
    rotated = []
    rad = math.radians(theta)

    for x, y in points :
        new_x = x * math.cos(rad) - y * math.sin(rad)
        new_y = x * math.sin(rad) + y * math.cos(rad)

        rotated.append((new_x, new_y))

    return rotated

# step-1 : Take the points 
points = [(1,2),(5,2), (3, 6)]

# Step-2 : Take Angle 
theta = 90

# Call The Function 
rotated = rotate(points, theta)

print(points)
print(rotated)

# STep-4 : Plot the original and rotated point
points += [points[0]]
rotated += [rotated[0]]
# Original point plot
plt.plot([p[0] for p in points], [p[1] for p in points], label = "Original", marker='s', color='green')
# Rotation point plot
plt.plot([p[0] for p in rotated], [p[1] for p in rotated], label = "Original", marker='o', color='red')

# Original coordinates
for x, y in points : 
    plt.text(x, y, f'({x}, {y})', color='green')

# Rotated coordinates
for x, y in rotated :
    plt.text(x, y, f'{x:.2f}, {y:.2f}', color='red')

plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.legend()
plt.title("2D Rotation")
plt.tight_layout()
plt.show()