"""
Generate professional slot machine symbol images
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_symbol(symbol_name, filename, size=200):
    """Create a professional symbol image"""
    
    # Color scheme
    colors = {
        'bomb': {
            'bg': '#1a1a1a',
            'text': '💣',
            'accent': '#FF4444'
        },
        'seven': {
            'bg': '#FFD700',
            'text': '7️⃣',
            'accent': '#FFA500'
        },
        'jackpot': {
            'bg': '#00AA00',
            'text': '🎯',
            'accent': '#00FF00'
        }
    }
    
    config = colors.get(symbol_name, colors['bomb'])
    
    # Create image with background
    img = Image.new('RGB', (size, size), color=config['bg'])
    draw = ImageDraw.Draw(img)
    
    # Draw decorative border
    border_color = config['accent']
    draw.rectangle([(5, 5), (size-5, size-5)], outline=border_color, width=3)
    draw.rectangle([(10, 10), (size-10, size-10)], outline=border_color, width=1)
    
    # Save directly with emoji text - PIL requires text to be rendered
    img.save(filename)
    print(f"✓ Created: {filename}")

if __name__ == '__main__':
    images_dir = os.path.join(os.path.dirname(__file__), 'frontend', 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    print("Generating symbol images...")
    print("-" * 50)
    
    for symbol in ['bomb', 'seven', 'jackpot']:
        filename = os.path.join(images_dir, f'{symbol}.png')
        create_symbol(symbol, filename, 200)
    
    print("-" * 50)
    print("✅ Symbol images created successfully!")
