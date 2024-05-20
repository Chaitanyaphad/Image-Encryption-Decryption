from Crypto.Cipher import DES, AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from PIL import Image
from Crypto.Util.Padding import pad, unpad

# Function to encrypt an image
def encrypt_image(image_path):
    # Read the image file
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Generate random keys for DES and AES
    des_key = get_random_bytes(8)
    aes_key = get_random_bytes(16)

    # Generate an RSA key pair (or load existing keys)
    rsa_key = RSA.generate(2048)

    # Encrypt the image using DES and AES
    des_cipher = DES.new(des_key, DES.MODE_CBC)
    aes_cipher = AES.new(aes_key, AES.MODE_CBC)

    # Ensure the image data is padded to a multiple of the block size
    image_data = pad(image_data, max(des_cipher.block_size, aes_cipher.block_size))

    encrypted_image_data = aes_cipher.iv + des_cipher.iv + aes_cipher.encrypt(des_cipher.encrypt(image_data))

    # Encrypt the DES and AES keys using RSA
    rsa_cipher = PKCS1_OAEP.new(rsa_key.publickey())
    encrypted_des_key = rsa_cipher.encrypt(des_key)
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    # Save the encrypted image and keys
    with open('encrypted_image.png', 'wb') as file:
        file.write(encrypted_image_data)

    with open('encrypted_des_key.bin', 'wb') as file:
        file.write(encrypted_des_key)

    with open('encrypted_aes_key.bin', 'wb') as file:
        file.write(encrypted_aes_key)

    with open('rsa_key.pem', 'wb') as file:
        file.write(rsa_key.export_key())

    print("Image encryption completed.")

# Function to decrypt an image
def decrypt_image():
    # Read the encrypted image
    with open('encrypted_image.png', 'rb') as file:
        encrypted_image_data = file.read()

    # Read the encrypted DES and AES keys
    with open('encrypted_des_key.bin', 'rb') as file:
        encrypted_des_key = file.read()

    with open('encrypted_aes_key.bin', 'rb') as file:
        encrypted_aes_key = file.read()

    # Read the RSA key
    with open('rsa_key.pem', 'rb') as file:
        rsa_key = RSA.import_key(file.read())

    # Decrypt the DES and AES keys using RSA
    rsa_cipher = PKCS1_OAEP.new(rsa_key)
    des_key = rsa_cipher.decrypt(encrypted_des_key)
    aes_key = rsa_cipher.decrypt(encrypted_aes_key)

    # Split IVs from encrypted image data
    aes_iv = encrypted_image_data[:16]
    des_iv = encrypted_image_data[16:24]
    encrypted_image_data = encrypted_image_data[24:]

    # Decrypt the image using DES and AES
    des_cipher = DES.new(des_key, DES.MODE_CBC, iv=des_iv)
    aes_cipher = AES.new(aes_key, AES.MODE_CBC, iv=aes_iv)

    decrypted_image_data = des_cipher.decrypt(aes_cipher.decrypt(encrypted_image_data))

    # Save the decrypted image
    with open('decrypted_image.png', 'wb') as file:
        file.write(unpad(decrypted_image_data, max(des_cipher.block_size, aes_cipher.block_size)))

    print("Image decryption completed.")

# Encrypt the image
encrypt_image('Sample.png')

# Decrypt the image
decrypt_image()