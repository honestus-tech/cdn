import os

base_url = "https://cdn.jsdelivr.net/gh/honestus-tech/cdn@main/material_images/"
assets_dir = "/Users/hackyroot/Desktop/honestus/cdn/material_images/"

with open('output.txt', 'w') as f:
    for filename in sorted(os.listdir(assets_dir)):        
        f.write(base_url + filename + '\n')
