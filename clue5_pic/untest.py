from PIL import Image

def extract_message_full(image_path):
    # Open the grayscale image
    img = Image.open(image_path).convert("L")
    width, height = img.size
    binary_data = ''

    # Loop through all pixels and extract the LSB
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            binary_data += str(pixel & 1)  # Extract the LSB

    print(binary_data)
    # Convert the binary data to text in chunks of 8 bits
    message = ''.join(
        chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)
    )
    
    # Return the full message (including potential padding)
    return message

print(chr(int('0b00000000',2)))

# Example usage
encoded_image_path = "encoded_image_grayscale.png"
extracted_message = extract_message_full(encoded_image_path)
print("Extracted message:", extracted_message)
