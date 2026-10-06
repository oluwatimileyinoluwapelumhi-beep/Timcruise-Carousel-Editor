"""
Example usage of the Carousel Editor
Shows different ways to use the tool
"""

from carousel_editor import CarouselEditor
from quotes_api import QuotesAPI

def example_1_single_image_random_quote():
    """Edit a single image with a random motivational quote"""
    print("Example 1: Single image with random quote")
    print("=" * 50)
    
    editor = CarouselEditor()
    
    # Place your Instagram downloaded image in the same folder as this script
    # and replace 'image.jpg' with your filename
    # editor.add_text_to_image("image.jpg")
    
    print("To use this example:")
    print("1. Download a motivational image from Instagram")
    print("2. Save it as 'image.jpg' in the project folder")
    print("3. Uncomment the line above and run this script")
    print()


def example_2_single_image_custom_quote():
    """Edit a single image with your custom quote"""
    print("Example 2: Single image with custom quote")
    print("=" * 50)
    
    editor = CarouselEditor()
    
    custom_quote = "Your journey to success starts with a single step"
    # editor.add_text_to_image("image.jpg", quote=custom_quote)
    
    print("To use this example:")
    print("1. Download a motivational image from Instagram")
    print("2. Save it as 'image.jpg' in the project folder")
    print("3. Modify the custom_quote variable with your message")
    print("4. Uncomment the line above and run this script")
    print()


def example_3_batch_edit():
    """Batch edit all images in a folder"""
    print("Example 3: Batch edit multiple images")
    print("=" * 50)
    
    editor = CarouselEditor()
    
    # Create a folder named 'images_to_edit' and place your images there
    # editor.batch_edit_images("images_to_edit")
    
    print("To use this example:")
    print("1. Create a folder named 'images_to_edit'")
    print("2. Download multiple motivational images from Instagram")
    print("3. Place them in the 'images_to_edit' folder")
    print("4. Uncomment the line above and run this script")
    print("5. All edited images will be saved to 'edited_posts' folder")
    print()


def example_4_fetch_online_quote():
    """Fetch a quote from online API"""
    print("Example 4: Fetch motivational quote from online")
    print("=" * 50)
    
    quotes_api = QuotesAPI()
    
    print("Fetching quote from Quotable.io API...")
    quote = quotes_api.get_quote_from_quotable()
    if quote:
        print(f"✓ Quote: {quote}")
        
        # Then use it with the editor
        # editor = CarouselEditor()
        # editor.add_text_to_image("image.jpg", quote=quote)
    else:
        print("✗ Could not fetch quote (check internet connection)")
    print()


def example_5_customize_branding():
    """Use different group name and creator name"""
    print("Example 5: Customize branding")
    print("=" * 50)
    
    # Create editor with custom branding
    editor = CarouselEditor(
        group_name="THE GROWTH NEXUS [INSIGHT & OUTLOOK]",
        creator_name="@Timilocruise"
    )
    
    # editor.add_text_to_image("image.jpg")
    
    print("To use this example:")
    print("1. The editor is configured with your group and personal branding")
    print("2. You can change these by modifying the CarouselEditor parameters")
    print()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TIMCRUISE CAROUSEL EDITOR - USAGE EXAMPLES")
    print("=" * 60 + "\n")
    
    example_1_single_image_random_quote()
    example_2_single_image_custom_quote()
    example_3_batch_edit()
    example_4_fetch_online_quote()
    example_5_customize_branding()
    
    print("=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Download motivational images from Instagram")
    print("3. Uncomment the examples above to try them")
    print("4. Check the 'edited_posts' folder for your branded images")
    print("5. Upload the edited images to your group!")
    print("=" * 60 + "\n")
