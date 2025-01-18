from PIL import Image

def hide_message_with_padding(image_path, output_path, message):
    # Open the image and convert to grayscale
    img = Image.open(image_path).convert("L")  # "L" mode is for grayscale
    encoded = img.copy()
    width, height = img.size
    total_pixels = width * height

    # Convert the message to binary
    message_binary = ''.join([format(ord(char), '08b') for char in message])

    # Pad the binary message to fit the entire image size
    if len(message_binary) < total_pixels:
        message_binary += '0' * (total_pixels - len(message_binary))
    elif len(message_binary) > total_pixels:
        raise ValueError("Message is too long to fit in the image.")

    # Loop through each pixel and encode the message
    binary_index = 0
    for y in range(height):
        for x in range(width):
            # Get the current pixel intensity (grayscale value)
            pixel = img.getpixel((x, y))

            # Modify the least significant bit
            pixel = (pixel & ~1) | int(message_binary[binary_index])
            binary_index += 1

            # Save the modified pixel back
            encoded.putpixel((x, y), pixel)

    # Save the encoded image
    encoded.save(output_path, "PNG")
    print(f"Message successfully hidden in {output_path}")

# Example usage
image_path = "papapetme.png"  # Replace with your input image
output_path = "encoded_image_grayscale.png"
message = "papa favourite is me"

hide_message_with_padding(image_path, output_path, message)
