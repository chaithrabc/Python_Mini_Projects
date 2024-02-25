#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image, ImageEnhance, ImageFilter

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(factor)
    return enhanced_image

def adjust_lightness(image, factor):
    enhancer = ImageEnhance.Color(image)
    enhanced_image = enhancer.enhance(factor)
    return enhanced_image

def adjust_darkness(image, factor):
    enhanced_image = adjust_lightness(image, factor)
    return enhanced_image

def apply_blur(image, radius):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=radius))
    return blurred_image

def main():
    # Load image
    image_path = "C:\\Users\\chand\\Downloads\\11. Photo manipulation\\images.jpg"  
    original_image = Image.open(image_path)

    # Display original image
    original_image.show()

    # Adjust brightness
    brightness_factor = 1.5
    brightened_image = adjust_brightness(original_image, brightness_factor)
    brightened_image.show()

    # Adjust lightness
    lightness_factor = 1.5
    lightened_image = adjust_lightness(original_image, lightness_factor)
    lightened_image.show()

    # Adjust darkness
    darkness_factor = 0.5
    darkened_image = adjust_darkness(original_image, darkness_factor)
    darkened_image.show()

    # Apply blur
    blur_radius = 2
    blurred_image = apply_blur(original_image, blur_radius)
    blurred_image.show()

if __name__ == "__main__":
    main()


# In[ ]:




