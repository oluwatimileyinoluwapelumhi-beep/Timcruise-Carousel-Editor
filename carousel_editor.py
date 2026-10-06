"""
Timcruise Carousel Editor
A tool to edit motivational posts and add branding
"""

from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
import random

class CarouselEditor:
    def __init__(self, group_name="THE GROWTH NEXUS [INSIGHT & OUTLOOK]", creator_name="@Timilocruise"):
        self.group_name = group_name
        self.creator_name = creator_name
        self.output_dir = "edited_posts"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # Motivational quotes database
        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Success is not final, failure is not fatal. - Winston Churchill",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "It does not matter how slowly you go as long as you do not stop. - Confucius",
            "Everything you want is on the other side of fear. - George Addair",
            "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "It is during our darkest moments that we must focus to see the light. - Aristotle",
            "The only impossible journey is the one you never begin. - Tony Robbins",
            "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
            "Your limitation—it's only your imagination. Push beyond limits.",
            "Great things never came from comfort zones.",
            "Dream it. Believe it. Build it.",
            "Success doesn't just find you. You have to go out and get it.",
            "The harder you work for something, the greater you'll feel when you achieve it.",
        ]
    
    def get_random_quote(self):
        """Get a random motivational quote"""
        return random.choice(self.quotes)
    
    def add_text_to_image(self, image_path, output_filename=None, quote=None):
        """
        Add branding text and optional quote to an image
        
        Args:
            image_path (str): Path to the image file
            output_filename (str): Name for the output file (optional)
            quote (str): Custom quote to add (if None, uses random quote)
        
        Returns:
            str: Path to the edited image
        """
        
        if not os.path.exists(image_path):
            print(f"Error: Image file '{image_path}' not found")
            return None
        
        # Open image
        image = Image.open(image_path)
        image = image.convert("RGB")
        width, height = image.size
        
        # Create a copy to edit
        edited_image = image.copy()
        draw = ImageDraw.Draw(edited_image)
        
        # Try to use a nice font, fall back to default if not available
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
            text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
            small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
        except:
            # Fallback to default font
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        # Get quote
        if quote is None:
            quote = self.get_random_quote()
        
        # Add semi-transparent overlay for text readability
        overlay = Image.new("RGBA", edited_image.size, (0, 0, 0, 180))
        edited_image.paste(overlay, (0, 0), overlay)
        draw = ImageDraw.Draw(edited_image)
        
        # Add quote in the middle
        quote_color = (255, 255, 255)  # White text
        self._draw_wrapped_text(draw, quote, text_font, quote_color, width, height, 0.3)
        
        # Add group name at bottom
        group_y = height - 120
        draw.text((20, group_y), self.group_name, fill=quote_color, font=title_font)
        
        # Add creator name
        creator_y = height - 60
        draw.text((20, creator_y), f"By: {self.creator_name}", fill=quote_color, font=small_font)
        
        # Generate output filename
        if output_filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"edited_post_{timestamp}.png"
        
        output_path = os.path.join(self.output_dir, output_filename)
        
        # Save edited image
        edited_image.save(output_path)
        print(f"✓ Image saved: {output_path}")
        
        return output_path
    
    def _draw_wrapped_text(self, draw, text, font, color, width, height, vertical_position):
        """Draw text with word wrapping"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            test_line = " ".join(current_line)
            # Estimate text width (rough approximation)
            if len(test_line) * 15 > width - 40:  # Rough width calculation
                if len(current_line) > 1:
                    current_line.pop()
                    lines.append(" ".join(current_line))
                    current_line = [word]
        
        if current_line:
            lines.append(" ".join(current_line))
        
        # Calculate starting Y position to center text
        line_height = 40
        total_height = len(lines) * line_height
        start_y = int(height * vertical_position - total_height / 2)
        
        # Draw each line
        for i, line in enumerate(lines):
            y = start_y + (i * line_height)
            # Center text horizontally (rough approximation)
            x = 20
            draw.text((x, y), line, fill=color, font=font)
    
    def batch_edit_images(self, image_folder):
        """
        Edit all images in a folder
        
        Args:
            image_folder (str): Path to folder containing images
        """
        if not os.path.isdir(image_folder):
            print(f"Error: Folder '{image_folder}' not found")
            return
        
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
        edited_count = 0
        
        for filename in os.listdir(image_folder):
            if os.path.splitext(filename)[1].lower() in image_extensions:
                image_path = os.path.join(image_folder, filename)
                print(f"Processing: {filename}")
                self.add_text_to_image(image_path, f"edited_{filename}")
                edited_count += 1
        
        print(f"\n✓ Processed {edited_count} images")


if __name__ == "__main__":
    # Example usage
    editor = CarouselEditor()
    
    # Example 1: Edit a single image with a custom quote
    # editor.add_text_to_image("your_image.jpg", quote="Your custom quote here")
    
    # Example 2: Edit a single image with random quote
    # editor.add_text_to_image("your_image.jpg")
    
    # Example 3: Batch edit all images in a folder
    # editor.batch_edit_images("images_folder")
    
    print("Carousel Editor Ready!")
    print("See README.md for usage instructions")
