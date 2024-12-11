# Enigma - CSV Compression and Encryption System

This project is a GUI-based application built using Python and Tkinter that allows users to:

1. **Compress and Encrypt** a CSV file:
   - Compresses the selected CSV file into a ZIP archive.
   - Encrypts the ZIP file using a randomly generated Fernet encryption key.
   - Displays the encryption key for secure storage.

2. **Decrypt and Decompress** an encrypted ZIP file:
   - Decrypts the provided encrypted ZIP file using a user-provided encryption key.
   - Decompresses the decrypted ZIP file to extract its contents.

---

## Features

- **File Compression**: Compress CSV files into ZIP archives.
- **Encryption**: Securely encrypt ZIP files using Fernet (AES encryption).
- **Decryption**: Decrypt ZIP files using the corresponding encryption key.
- **File Decompression**: Extract files from decrypted ZIP archives.
- **User-Friendly Interface**: A graphical interface for seamless interaction.
- **Key Management**: Generates and displays encryption keys, with clipboard copy functionality.

---

## Requirements

- Python 3.7 or higher
- Required Python modules:
  - `tkinter`
  - `ttk`
  - `filedialog`
  - `messagebox`
  - `scrolledtext`
  - `os`
  - `zipfile`
  - `cryptography` (Install via `pip install cryptography`)

---

## How to Use

### 1. Compress & Encrypt a CSV File
1. Launch the application.
2. In the **Compress & Encrypt CSV** section:
   - Click **Browse** to select the CSV file.
   - Click **Browse** to choose the output folder.
   - Click **Compress & Encrypt CSV**.
3. The encrypted ZIP file will be saved in the output folder, and the encryption key will be displayed in the text box. Copy and securely store the encryption key.

### 2. Decrypt & Decompress an Encrypted ZIP File
1. Launch the application.
2. In the **Decrypt & Decompress ZIP** section:
   - Click **Browse** to select the encrypted ZIP file.
   - Enter the encryption key used during the file encryption process.
   - Click **Browse** to choose the output folder.
   - Click **Decrypt & Decompress ZIP**.
3. The decrypted and decompressed files will be extracted to the selected output folder.

---

## Notes

- **Key Security**: The encryption key is crucial for decryption. Losing the key will make it impossible to decrypt the files.
- **File Formats**: The application only supports CSV files for compression and encryption.

---

![Screenshot (298)](https://github.com/user-attachments/assets/46428c30-5ca5-4f02-96a8-52323ad43e8f)
![Screenshot (299)](https://github.com/user-attachments/assets/b58880de-cdbf-4cac-95cc-75e5f6803a5b)

