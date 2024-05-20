# Image-Encryption-Decryption
This project demonstrates a method to encrypt and decrypt images using a combination of DES, AES, and RSA encryption algorithms. The image is first encrypted using DES and AES, and the encryption keys are then securely encrypted using RSA.

# Description
This project demonstrates a method to encrypt and decrypt images using a combination of DES, AES, and RSA encryption algorithms. The image is first encrypted using DES and AES, and the encryption keys are then securely encrypted using RSA.

# Features
<ul>
  1. Encrypt an image using DES and AES encryption algorithms. <br>
  2. Securely encrypt DES and AES keys using RSA. <br>
  3. Decrypt the image using the encrypted keys. <br>
</ul>

# Prerequisites
Ensure you have the following installed:
<ul> 
  1. Python 3.x <br>
  2. pycryptodome library <br>
  3. Pillow library <br>
</ul>

You can install the required libraries using pip: 
pip install pycryptodome Pillow

# Usage
1. Place the image you want to encrypt in the project directory. <br>
2. Rename the image to Sample.png or modify the encrypt_image function to use your image file name.<br>
3. Run the encryption script:<br>
4. The encrypted image and keys will be saved in the project directory. <br>
5. To decrypt the image, ensure the encrypted image and keys are in the project directory and run the decryption function. <br>
6. The decrypted image will be saved as decrypted_image.png.<br>

