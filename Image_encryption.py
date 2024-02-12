from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    encrypted_image = image.copy()

    pixels = encrypted_image.load()
    width, height = encrypted_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r += key
            g += key
            b += key

            # Constrain RGB values to the valid range (0-255)
            r = min(max(r, 0), 255)
            g = min(max(g, 0), 255)
            b = min(max(b, 0), 255)

            pixels[x, y] = (r, g, b)

    return encrypted_image

def decrypt_image(encrypted_image_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    decrypted_image = encrypted_image.copy()

    pixels = decrypted_image.load()
    width, height = decrypted_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r -= key
            g -= key
            b -= key

            # Constrain RGB values to the valid range (0-255)
            r = min(max(r, 0), 255)
            g = min(max(g, 0), 255)
            b = min(max(b, 0), 255)

            pixels[x, y] = (r, g, b)

    return decrypted_image

def main():
    image_path = "input_image.png"
    key = 10

    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    encrypted_image.save("encrypted_image.png")

    # Decrypt the image
    decrypted_image = decrypt_image("encrypted_image.png", key)
    decrypted_image.save("decrypted_image.png")

if __name__ == "__main__":
    main()