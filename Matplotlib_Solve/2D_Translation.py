import matplotlib.pyplot as plt

# Step-3 : Calculation Translation 
def translate(points, tx, ty):
    translated = []

    for x , y in points :
        new_x = x + tx
        new_y = y + ty
        translated.append((new_x, new_y))

    return translated
    
# Step-1 : Take Point 
points = [(2, 3), (4,4), (2,7)]

# Step-2 : Take Translation Vector
tx , ty = 3, 2

# Call The Function
translated = translate(points , tx, ty)

# Step-4 : Plot the Original and Translated points
# Plot preparation 
points += [points[0]]
translated += [translated[0]]
print(points)
print(translated)

# Plot Original points
plt.plot([p[0] for p in points], [p[1] for p in points], marker = 's', label = "Original")

# Plot Translated point 
plt.plot([p[0] for p in translated], [p[1] for p in translated], marker = 'o', label = "Translated")

plt.legend()
plt.grid()
plt.title("2D Translation")
plt.tight_layout()
plt.show()
