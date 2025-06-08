import random
import os

def generate_svg(num_dots, filename):
    svg_content = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
'''
    
    for _ in range(num_dots):
        x = random.randint(50, 462)  # Keep dots away from edges
        y = random.randint(50, 462)
        size = random.randint(10, 40)  # Random size between 10 and 40
        svg_content += f'  <circle cx="{x}" cy="{y}" r="{size}" fill="#FF69B4" />\n'
    
    svg_content += '</svg>'
    
    with open(filename, 'w') as f:
        f.write(svg_content)

# Create dots directory if it doesn't exist
os.makedirs('dots', exist_ok=True)

# Generate 18 SVG files with 3 to 20 dots
for i in range(3, 21):
    filename = f'dots/dots_{i}.svg'
    generate_svg(i, filename) 