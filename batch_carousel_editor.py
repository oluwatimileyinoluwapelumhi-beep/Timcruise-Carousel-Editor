"""
Batch carousel editor with multiple image import and export
Supports both motivational posts and Storipod story editing
"""

from PIL import Image, ImageDraw, ImageFont
import os
import random
from datetime import datetime
import glob

class BatchCarouselEditor:
    def __init__(self, group_name="THE GROWTH NEXUS [INSIGHT & OUTLOOK]", creator_name="@Timilocruise"):
        self.group_name = group_name
        self.creator_name = creator_name
        self.output_dir = "edited_posts"
        self.storipod_output_dir = "storipod_edits"
        
        # Create output directories
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.storipod_output_dir, exist_ok=True)
        
        # Motivational quotes for social media
        self.motivational_quotes = [
            "The only way to do great work is to love what you do.",
            "Success is not final, failure is not fatal.",
            "Believe you can and you're halfway there.",
            "It does not matter how slowly you go as long as you do not stop.",
            "Everything you want is on the other side of fear.",
            "Don't watch the clock; do what it does. Keep going.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "It is during our darkest moments that we must focus to see the light.",
            "The only impossible journey is the one you never begin.",
            "Success usually comes to those who are too busy to be looking for it.",
            "Your limitation—it's only your imagination.",
            "Great things never came from comfort zones.",
            "Dream it. Believe it. Build it.",
            "Success doesn't just find you. You have to go out and get it.",
            "The harder you work for something, the greater you'll feel when you achieve it.",
        ]
        
        # Storipod story watermarks and quotes
        self.storipod_quotes = [
            "Read my full story on Storipod",
            "Continue reading on Storipod",
            "Follow me on Storipod for more",
            "This story continues on Storipod",
            "Get the full story on Storipod",
        ]
    
    def get_random_quote(self, quote_type="motivational"):
        """Get a random quote based on type"""
        if quote_type == "storipod":
            return random.choice(self.storipod_quotes)
        return random.choice(self.motivational_quotes)
    
    def load_fonts(self):
        """Load fonts with fallback"""
        try:
            title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
            text_font = ImageFont.truetype("DejaVuSans.ttf", 32)
            small_font = ImageFont.truetype("DejaVuSans.ttf", 24)
            watermark_font = ImageFont.truetype("DejaVuSans.ttf", 28)
        except:
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
            watermark_font = ImageFont.load_default()
        
        return title_font, text_font, small_font, watermark_font
    
    def edit_image_motivational(self, image_path, output_filename=None, quote=None):
        """
        Edit image for motivational posts (Facebook/Instagram)
        """
        if not os.path.exists(image_path):
            print(f"✗ Error: Image '{image_path}' not found")
            return None
        
        try:
            image = Image.open(image_path).convert("RGB")
            width, height = image.size
            
            # Add semi-transparent overlay
            overlay = Image.new("RGBA", image.size, (0, 0, 0, 180))
            base = image.convert("RGBA")
            image = Image.alpha_composite(base, overlay).convert("RGB")
            draw = ImageDraw.Draw(image)
            
            title_font, text_font, small_font, _ = self.load_fonts()
            
            # Get quote
            if quote is None:
                quote = self.get_random_quote("motivational")
            
            # Draw quote
            self._draw_wrapped_text(draw, quote, text_font, (255, 255, 255), width, height, 0.35)
            
            # Draw group name
            draw.text((20, height - 120), self.group_name, fill=(255, 255, 255), font=title_font)
            
            # Draw creator name
            draw.text((20, height - 60), f"By: {self.creator_name}", fill=(255, 255, 255), font=small_font)
            
            # Generate output filename
            if output_filename is None:
                base_name = os.path.splitext(os.path.basename(image_path))[0]
                output_filename = f"{base_name}_motivational.png"
            
            output_path = os.path.join(self.output_dir, output_filename)
            image.save(output_path, "PNG", quality=95)
            print(f"✓ Saved motivational: {output_filename}")
            
            return output_path
            
        except Exception as e:
            print(f"✗ Error processing {image_path}: {str(e)}")
            return None
    
    def edit_image_storipod(self, image_path, output_filename=None, story_title=None, promo_text=None):
        """
        Edit image for Storipod story promotion
        Adds story title and promo watermark
        """
        if not os.path.exists(image_path):
            print(f"✗ Error: Image '{image_path}' not found")
            return None
        
        try:
            image = Image.open(image_path).convert("RGB")
            width, height = image.size
            
            # Add semi-transparent overlay (lighter for story content)
            overlay = Image.new("RGBA", image.size, (0, 0, 0, 150))
            base = image.convert("RGBA")
            image = Image.alpha_composite(base, overlay).convert("RGB")
            draw = ImageDraw.Draw(image)
            
            title_font, text_font, small_font, watermark_font = self.load_fonts()
            
            # Draw story title (if provided)
            if story_title:
                self._draw_wrapped_text(draw, story_title, title_font, (255, 215, 0), width, height, 0.3)
            
            # Draw promo text or default Storipod watermark
            if promo_text is None:
                promo_text = self.get_random_quote("storipod")
            
            draw.text((20, height - 100), promo_text, fill=(255, 215, 0), font=watermark_font)
            
            # Add Storipod branding
            draw.text((20, height - 50), "📖 Storipod Stories", fill=(255, 215, 0), font=small_font)
            
            # Generate output filename
            if output_filename is None:
                base_name = os.path.splitext(os.path.basename(image_path))[0]
                output_filename = f"{base_name}_storipod.png"
            
            output_path = os.path.join(self.storipod_output_dir, output_filename)
            image.save(output_path, "PNG", quality=95)
            print(f"✓ Saved Storipod promo: {output_filename}")
            
            return output_path
            
        except Exception as e:
            print(f"✗ Error processing {image_path}: {str(e)}")
            return None
    
    def _draw_wrapped_text(self, draw, text, font, color, width, height, vertical_position):
        """Draw text with word wrapping"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            test_line = " ".join(current_line)
            if len(test_line) * 15 > width - 60:
                if len(current_line) > 1:
                    current_line.pop()
                    lines.append(" ".join(current_line))
                    current_line = [word]
        
        if current_line:
            lines.append(" ".join(current_line))
        
        line_height = 45
        total_height = len(lines) * line_height
        start_y = int(height * vertical_position - total_height / 2)
        
        for i, line in enumerate(lines):
            y = start_y + (i * line_height)
            draw.text((30, y), line, fill=color, font=font)
    
    def batch_edit_motivational(self, image_folder, output_prefix=""):
        """Edit all images in a folder for motivational posts"""
        if not os.path.isdir(image_folder):
            print(f"✗ Error: Folder '{image_folder}' not found")
            return
        
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
        edited_count = 0
        
        print(f"\n📸 Batch editing images from: {image_folder}")
        print("=" * 50)
        
        for filename in sorted(os.listdir(image_folder)):
            if os.path.splitext(filename)[1].lower() in image_extensions:
                image_path = os.path.join(image_folder, filename)
                output_name = f"{output_prefix}{filename}" if output_prefix else f"motivational_{filename}"
                self.edit_image_motivational(image_path, output_name)
                edited_count += 1
        
        print("=" * 50)
        print(f"✓ Processed {edited_count} images for motivational posts")
        print(f"📁 Saved to: {self.output_dir}/\n")
    
    def batch_edit_storipod(self, image_folder, output_prefix=""):
        """Edit all images in a folder for Storipod story promos"""
        if not os.path.isdir(image_folder):
            print(f"✗ Error: Folder '{image_folder}' not found")
            return
        
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}
        edited_count = 0
        
        print(f"\n📖 Batch editing images for Storipod from: {image_folder}")
        print("=" * 50)
        
        for filename in sorted(os.listdir(image_folder)):
            if os.path.splitext(filename)[1].lower() in image_extensions:
                image_path = os.path.join(image_folder, filename)
                output_name = f"{output_prefix}{filename}" if output_prefix else f"storipod_{filename}"
                self.edit_image_storipod(image_path, output_name)
                edited_count += 1
        
        print("=" * 50)
        print(f"✓ Processed {edited_count} images for Storipod")
        print(f"📁 Saved to: {self.storipod_output_dir}/\n")
    
    def download_all_edited(self):
        """Create a summary of all edited images"""
        print("\n📥 Summary of edited images:")
        print("=" * 50)
        
        motivational_files = os.listdir(self.output_dir) if os.path.exists(self.output_dir) else []
        storipod_files = os.listdir(self.storipod_output_dir) if os.path.exists(self.storipod_output_dir) else []
        
        if motivational_files:
            print(f"\n📱 Motivational/Facebook/Instagram posts ({len(motivational_files)}):")
            for f in motivational_files:
                print(f"  ✓ {self.output_dir}/{f}")
        
        if storipod_files:
            print(f"\n📖 Storipod promo images ({len(storipod_files)}):")
            for f in storipod_files:
                print(f"  ✓ {self.storipod_output_dir}/{f}")
        
        print("=" * 50)


if __name__ == "__main__":
    editor = BatchCarouselEditor()
    
    print("\n" + "=" * 60)
    print("TIMCRUISE BATCH CAROUSEL EDITOR - DUAL MODE")
    print("=" * 60)
    print("\nSupports:")
    print("  1. Motivational posts for Facebook/Instagram")
    print("  2. Storipod story promotion edits")
    print("\nSee example_usage.py for detailed instructions")
    print("=" * 60 + "\n")
