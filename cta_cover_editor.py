"""
Call-to-Action (CTA) Cover Editor
Creates promotional graphics to drive engagement and followers
Links viewers to your Facebook group, profile, and Storipod
"""

from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime


class CTACoverEditor:
    def __init__(self, group_name="THE GROWTH NEXUS [INSIGHT & OUTLOOK]", creator_name="@Timilocruise"):
        self.group_name = group_name
        self.creator_name = creator_name
        self.output_dir = "cta_covers"
        
        # Your actual links
        self.storipod_link = "https://storipod.app/user/emmanueloluwati"
        self.facebook_group_link = "https://www.facebook.com/share/g/1DP4fBrw7K/"
        self.facebook_profile_link = "https://www.facebook.com/share/1CFY4gyV4h/"
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        # CTA templates with different messages
        self.cta_templates = {
            "like_follow_share": {
                "title": "JOIN OUR COMMUNITY",
                "lines": [
                    "👍 LIKE THIS POST",
                    "🔔 FOLLOW FOR MORE",
                    "📢 SHARE WITH FRIENDS"
                ]
            },
            "group_invite": {
                "title": "JOIN OUR GROWTH GROUP",
                "lines": [
                    "Be part of THE GROWTH NEXUS",
                    "Daily motivational content",
                    "Community support & growth"
                ]
            },
            "storipod_invite": {
                "title": "READ MY FULL STORY",
                "lines": [
                    "📖 Continue on Storipod",
                    "Exclusive content",
                    "Follow for more stories"
                ]
            },
            "multi_platform": {
                "title": "CONNECT WITH ME",
                "lines": [
                    "📱 Follow on Facebook",
                    "📖 Read on Storipod",
                    "🌟 Join the Movement"
                ]
            }
        }
    
    def load_fonts(self):
        """Load fonts with fallback"""
        try:
            title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
            text_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
            link_font = ImageFont.truetype("DejaVuSans.ttf", 28)
            small_font = ImageFont.truetype("DejaVuSans.ttf", 22)
        except:
            title_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
            link_font = ImageFont.load_default()
            small_font = ImageFont.load_default()
        
        return title_font, text_font, link_font, small_font
    
    def create_cta_cover(self, template_type="like_follow_share", output_filename=None, custom_title=None):
        """
        Create a colorful CTA cover from scratch (no background image needed)
        
        Args:
            template_type: Type of CTA template to use
            output_filename: Name for the output file
            custom_title: Custom title to override template title
        """
        
        # Create a vibrant gradient background
        width, height = 1080, 1350  # Instagram story size
        
        # Create base image with gradient colors
        image = Image.new("RGB", (width, height), color=(20, 120, 200))  # Blue base
        draw = ImageDraw.Draw(image)
        
        # Add gradient overlay with shapes
        for y in range(height):
            ratio = y / height
            r = int(20 + (255 - 20) * ratio)
            g = int(120 + (150 - 120) * ratio)
            b = int(200 + (100 - 200) * ratio)
            draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))
        
        title_font, text_font, link_font, small_font = self.load_fonts()
        
        # Get template
        if template_type not in self.cta_templates:
            template_type = "like_follow_share"
        
        template = self.cta_templates[template_type]
        title = custom_title or template["title"]
        lines = template["lines"]
        
        # Draw title with shadow effect
        title_y = 120
        draw.text((50, title_y + 3), title, fill=(0, 0, 0), font=title_font)  # Shadow
        draw.text((50, title_y), title, fill=(255, 215, 0), font=title_font)  # Gold text
        
        # Draw CTA lines
        line_y = title_y + 150
        for line in lines:
            draw.text((60, line_y + 2), line, fill=(0, 0, 0), font=text_font)  # Shadow
            draw.text((60, line_y), line, fill=(255, 255, 255), font=text_font)  # White text
            line_y += 100
        
        # Draw links section
        links_y = line_y + 80
        draw.text((50, links_y), "FOLLOW ME ON:", fill=(255, 215, 0), font=link_font)
        
        links_y += 70
        # Facebook group link
        draw.text((60, links_y + 1), "📱 Facebook Group", fill=(0, 0, 0), font=small_font)
        draw.text((60, links_y), "📱 Facebook Group", fill=(255, 255, 255), font=small_font)
        draw.text((60, links_y + 40), self.facebook_group_link, fill=(173, 216, 230), font=small_font)
        
        links_y += 100
        # Storipod link
        draw.text((60, links_y + 1), "📖 Storipod Stories", fill=(0, 0, 0), font=small_font)
        draw.text((60, links_y), "📖 Storipod Stories", fill=(255, 255, 255), font=small_font)
        draw.text((60, links_y + 40), self.storipod_link, fill=(173, 216, 230), font=small_font)
        
        links_y += 100
        # Facebook profile link
        draw.text((60, links_y + 1), "👤 Facebook Profile", fill=(0, 0, 0), font=small_font)
        draw.text((60, links_y), "👤 Facebook Profile", fill=(255, 255, 255), font=small_font)
        draw.text((60, links_y + 40), self.facebook_profile_link, fill=(173, 216, 230), font=small_font)
        
        # Add branding at bottom
        brand_y = height - 80
        draw.text((50, brand_y + 2), self.group_name, fill=(0, 0, 0), font=small_font)
        draw.text((50, brand_y), self.group_name, fill=(255, 215, 0), font=small_font)
        
        # Generate output filename
        if output_filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"cta_{template_type}_{timestamp}.png"
        
        output_path = os.path.join(self.output_dir, output_filename)
        image.save(output_path, "PNG", quality=95)
        print(f"✓ CTA Cover created: {output_filename}")
        
        return output_path
    
    def create_cta_from_image(self, image_path, template_type="like_follow_share", output_filename=None):
        """
        Create a CTA overlay on top of an existing image
        
        Args:
            image_path: Path to background image
            template_type: Type of CTA template
            output_filename: Name for output file
        """
        
        if not os.path.exists(image_path):
            print(f"✗ Error: Image '{image_path}' not found")
            return None
        
        try:
            image = Image.open(image_path).convert("RGB")
            width, height = image.size
            
            # Add semi-transparent overlay for text readability
            overlay = Image.new("RGBA", image.size, (0, 0, 0, 200))
            base = image.convert("RGBA")
            image = Image.alpha_composite(base, overlay).convert("RGB")
            draw = ImageDraw.Draw(image)
            
            title_font, text_font, link_font, small_font = self.load_fonts()
            
            # Get template
            if template_type not in self.cta_templates:
                template_type = "like_follow_share"
            
            template = self.cta_templates[template_type]
            title = template["title"]
            lines = template["lines"]
            
            # Draw title
            title_y = 100
            draw.text((40, title_y), title, fill=(255, 215, 0), font=title_font)
            
            # Draw CTA lines
            line_y = title_y + 120
            for line in lines:
                draw.text((50, line_y), line, fill=(255, 255, 255), font=text_font)
                line_y += 80
            
            # Draw links
            links_y = line_y + 60
            draw.text((40, links_y), "📱 " + self.facebook_group_link, fill=(173, 216, 230), font=link_font)
            draw.text((40, links_y + 60), "📖 " + self.storipod_link, fill=(173, 216, 230), font=link_font)
            
            # Generate output filename
            if output_filename is None:
                base_name = os.path.splitext(os.path.basename(image_path))[0]
                output_filename = f"{base_name}_cta.png"
            
            output_path = os.path.join(self.output_dir, output_filename)
            image.save(output_path, "PNG", quality=95)
            print(f"✓ CTA overlay created: {output_filename}")
            
            return output_path
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return None


if __name__ == "__main__":
    editor = CTACoverEditor()
    
    print("\n" + "=" * 60)
    print("CTA COVER EDITOR - ENGAGEMENT GRAPHICS")
    print("=" * 60)
    print("\nAvailable templates:")
    print("  - like_follow_share")
    print("  - group_invite")
    print("  - storipod_invite")
    print("  - multi_platform")
    print("\nSee main.py for usage instructions")
    print("=" * 60 + "\n")
