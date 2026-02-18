"""
Generate simple symbol images for slot machine game.
This script creates PNG files for each symbol.

Install PIL first: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def ensure_dir(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_simple_symbol(emoji, filename, size=200):
    """Create a simple symbol image with emoji."""
    # Create a white background image
    img = Image.new('RGBA', (size, size), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a colored background circle
    colors = {
        '💣': (255, 50, 50),      # Red for bomb
        '7️⃣': (255, 215, 0),     # Gold for seven
        '🎯': (30, 144, 255),     # Blue for jackpot
        '🍒': (220, 20, 60),      # Crimson for cherry
        '💎': (100, 149, 237),    # Cornflower for diamond
        '🏆': (255, 165, 0),      # Orange for gold/trophy
    }
    
    color = colors.get(emoji, (100, 149, 237))
    
    # Draw background circle
    margin = 20
    draw.ellipse([(margin, margin), (size-margin, size-margin)], 
                 fill=color, outline=(50, 50, 50), width=3)
    
    # Write emoji text in center
    try:
        # Try to use system font
        font_size = size // 2
        font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Save image
    img.save(filename)
    print(f"Created: {filename}")

def generate_all_symbols(images_dir):
    """Generate all default symbol images."""
    ensure_dir(images_dir)
    
    symbols = {
        'bomb': '💣',
        'seven': '7️⃣',
        'jackpot': '🎯',
        'cherry': '🍒',
        'diamond': '💎',
        'gold': '🏆',
    }
    
    for name, emoji in symbols.items():
        filename = os.path.join(images_dir, f'{name}.png')
        create_colored_symbol(name, filename, 200)

def create_colored_symbol(symbol_name, filename, size=200):
    """Create colored background symbols."""
    img = Image.new('RGB', (size, size), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Define colors for each symbol
    color_map = {
        'bomb': (220, 20, 60),        # Crimson red
        'seven': (255, 215, 0),       # Gold
        'jackpot': (30, 144, 255),    # Dodger blue
        'cherry': (255, 20, 147),     # Deep pink
        'diamond': (138, 43, 226),    # Blue violet
        'gold': (255, 140, 0),        # Dark orange
    }
    
    emoji_map = {
        'bomb': '💣',
        'seven': '7',
        'jackpot': '💰',
        'cherry': '🍒',
        'diamond': '💎',
        'gold': '🏆',
    }
    
    color = color_map.get(symbol_name, (100, 100, 100))
    emoji = emoji_map.get(symbol_name, '?')
    
    # Draw rounded rectangle background
    margin = 10
    draw.rectangle([(margin, margin), (size-margin, size-margin)], 
                   fill=color, outline=(50, 50, 50), width=3)
    
    # Add gradient effect (simplified - just darker border)
    draw.rectangle([(margin-1, margin-1), (size-margin+1, size-margin+1)], 
                   outline=(30, 30, 30), width=2)
    
    # Add text/number for symbols
    text_map = {
        'bomb': '💣',
        'seven': '7',
        'jackpot': '$',
        'cherry': '🍒',
        'diamond': '◆',
        'gold': '★',
    }
    
    text = text_map.get(symbol_name, symbol_name[0].upper())
    
    # Save image
    img.save(filename)
    print(f"Created: {filename}")

if __name__ == '__main__':
    # Get the images directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, 'frontend', 'images')
    
    print("Generating symbol images...")
    print("-" * 40)
    
    symbols = {
        'bomb': (220, 20, 60),        # Crimson
        'seven': (255, 215, 0),       # Gold
        'jackpot': (30, 144, 255),    # Blue
        'cherry': (255, 20, 147),     # Pink
        'diamond': (138, 43, 226),    # Purple
        'gold': (255, 140, 0),        # Orange
    }
    
    ensure_dir(images_dir)
    
    for symbol_name, color in symbols.items():
        filename = os.path.join(images_dir, f'{symbol_name}.png')
        create_colored_symbol(symbol_name, filename, 200)
    
    print("-" * 40)
    print("✅ Symbol images created successfully!")
    print(f"Images saved to: {images_dir}")
    print("\nYou can replace these with custom images:")
    print("- bomb.png")
    print("- seven.png")
    print("- jackpot.png")
    print("- cherry.png")
    print("- diamond.png")
    print("- gold.png")
