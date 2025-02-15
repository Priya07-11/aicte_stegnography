from PIL import Image

# Function to extract the hidden message from the PNG image
def extract_message(image_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()  # Get the image's pixels
    
    binary_message = ""
    
    # Iterate over all the pixels in the image
    for y in range(image.height):
        for x in range(image.width):
            # Get the current pixel (R, G, B)
            r, g, b = image.getpixel((x, y))
            
            # Extract the LSB from each color channel
            binary_message += str(r & 1)  # LSB of red
            binary_message += str(g & 1)  # LSB of green
            binary_message += str(b & 1)  # LSB of blue
    
    # Find the delimiter (end of message) to stop reading the message
    delimiter = '1111111111111110'
    end_index = binary_message.find(delimiter)
    if end_index != -1:
        binary_message = binary_message[:end_index]  # Trim the message to exclude delimiter
    else:
        print("Delimiter not found. No hidden message in this image.")
        return None

    # Convert the binary message back to text (characters)
    hidden_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        hidden_message += chr(int(byte, 2))
    
    return hidden_message


# Example usage
image_path = input("Enter the encoded PNG image path to extract the hidden message: ")
hidden_message = extract_message(image_path)

if hidden_message:
    print(f"Hidden message: {hidden_message}")