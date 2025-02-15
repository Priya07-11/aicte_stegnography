from PIL import Image

def hide_message(image_path, secret_message, output_image_path):
    
    image = Image.open(image_path)
    pixels = image.load()  # Load the image pixels
    
    
    binary_message = ''.join(format(ord(i), '08b') for i in secret_message)
    binary_message += '1111111111111110'  
    
    
    if len(binary_message) > image.width * image.height * 3:
        print("Message is too large for the given image.")
        return
    
    message_index = 0
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            
            if message_index < len(binary_message):
                r = (r & 0xFE) | int(binary_message[message_index])  
                message_index += 1
            if message_index < len(binary_message):
                g = (g & 0xFE) | int(binary_message[message_index])  
                message_index += 1
            if message_index < len(binary_message):
                b = (b & 0xFE) | int(binary_message[message_index])  
                message_index += 1
            
            
            image.putpixel((x, y), (r, g, b))
            
            if message_index >= len(binary_message):
                break
        if message_index >= len(binary_message):
            break
    
    
    image.save(output_image_path, format="PNG")
    print(f"Message hidden in image and saved as {output_image_path}")


image_path = input("Enter the image path to hide the message: ")
secret_message = input("Enter the secret message to hide: ")
output_image_path = input("Enter the output image path (with .png extension): ")

hide_message(image_path, secret_message, output_image_path)
