"""
Create cute food symbol images for slot machine
"""
from PIL import Image, ImageDraw
import os

def create_tofu_image(filename, size=200):
    """Create a simple tofu character image"""
    img = Image.new('RGBA', (size, size), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Tofu background (white/cream)
    draw.rectangle([(20, 30), (size-20, size-40)], fill='#F5E6D3', outline='#D4AF8F', width=2)
    
    # Green onions on top
    onion_positions = [(40, 15), (80, 10), (120, 15), (160, 12)]
    for x, y in onion_positions:
        draw.ellipse([(x-8, y), (x+8, y+20)], fill='#90EE90', outline='#6BBF59', width=1)
    
    # Eyes
    draw.ellipse([(50, 60), (70, 85)], fill='#333333')
    draw.ellipse([(130, 60), (150, 85)], fill='#333333')
    draw.ellipse([(58, 65), (62, 70)], fill='white')
    draw.ellipse([(138, 65), (142, 70)], fill='white')
    
    # Smile
    draw.arc([(60, 95), (140, 145)], 0, 180, fill='#333333', width=3)
    
    # Blush
    draw.ellipse([(35, 90), (50, 105)], fill='#FFB6C1')
    draw.ellipse([(150, 90), (165, 105)], fill='#FFB6C1')
    
    img.save(filename)
    print(f"✓ Created: {filename}")

def create_dango_image(filename, size=200):
    """Create a cute dango (candied fruit balls) image"""
    img = Image.new('RGBA', (size, size), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Stick
    draw.rectangle([(90, 10), (110, size-20)], fill='#8B4513')
    
    # Three dango balls
    ball_positions = [(size//2, 50), (size//2, 100), (size//2, 150)]
    
    for x, y in ball_positions:
        # Ball
        draw.ellipse([(x-35, y-35), (x+35, y+35)], fill='#FFA500', outline='#FF8C00', width=2)
        
        # Shine
        draw.ellipse([(x-20, y-20), (x-5, y-5)], fill='#FFD700', outline=None)
        
        # Eyes
        draw.ellipse([(x-15, y-5), (x-5, y+5)], fill='#333333')
        draw.ellipse([(x+5, y-5), (x+15, y+5)], fill='#333333')
        draw.ellipse([(x-12, y-2), (x-8, y+2)], fill='white')
        draw.ellipse([(x+8, y-2), (x+12, y+2)], fill='white')
        
        # Big smile
        draw.arc([(x-15, y+5), (x+15, y+25)], 0, 180, fill='#333333', width=2)
        
        # Blush
        draw.ellipse([(x-25, y), (x-15, y+10)], fill='#FFB6C1')
        draw.ellipse([(x+15, y), (x+25, y+10)], fill='#FFB6C1')
    
    img.save(filename)
    print(f"✓ Created: {filename}")

def create_soup_image(filename, size=200):
    """Create a cute soup jar image"""
    img = Image.new('RGBA', (size, size), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Jar outline
    draw.rectangle([(40, 50), (160, 170)], fill='#F5E6D3', outline='#8B7355', width=3)
    
    # Lid
    draw.rectangle([(50, 35), (150, 50)], fill='#D4AF8F', outline='#8B7355', width=2)
    draw.rectangle([(45, 30), (155, 40)], fill='#C9A961', outline='#8B7355', width=1)
    
    # Soup broth
    draw.rectangle([(45, 70), (155, 160)], fill='#F5DEB3')
    
    # Ingredients in soup
    # Red peppers
    pepper_positions = [(70, 110), (110, 120), (85, 135), (130, 100)]
    for x, y in pepper_positions:
        draw.ellipse([(x-10, y-8), (x+10, y+15)], fill='#DC143C')
    
    # Green onions/vegetables
    green_positions = [(80, 95), (120, 115), (100, 140), (75, 125)]
    for x, y in green_positions:
        draw.ellipse([(x-6, y-6), (x+6, y+10)], fill='#90EE90')
    
    # Water reflection
    draw.arc([(50, 65), (150, 100)], 0, 180, fill='#FFFFFF', width=2)
    
    # Eyes above jar
    draw.ellipse([(70, 50), (85, 65)], fill='#333333')
    draw.ellipse([(115, 50), (130, 65)], fill='#333333')
    draw.ellipse([(75, 55), (80, 60)], fill='white')
    draw.ellipse([(120, 55), (125, 60)], fill='white')
    
    # Smile
    draw.arc([(75, 65), (125, 85)], 0, 180, fill='#333333', width=2)
    
    # Blush
    draw.ellipse([(60, 60), (70, 70)], fill='#FFB6C1')
    draw.ellipse([(130, 60), (140, 70)], fill='#FFB6C1')
    
    # Hands
    draw.ellipse([(25, 90), (45, 105)], fill='#F5DEB3', outline='#8B7355', width=1)
    draw.ellipse([(155, 90), (175, 105)], fill='#F5DEB3', outline='#8B7355', width=1)
    
    img.save(filename)
    print(f"✓ Created: {filename}")

if __name__ == '__main__':
    images_dir = os.path.join(os.path.dirname(__file__), 'frontend', 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    print("Generating cute food symbol images...")
    print("-" * 50)
    
    create_tofu_image(os.path.join(images_dir, 'tofu.png'), 200)
    create_dango_image(os.path.join(images_dir, 'dango.png'), 200)
    create_soup_image(os.path.join(images_dir, 'soup.png'), 200)
    
    print("-" * 50)
    print("✅ Food symbol images created successfully!")
