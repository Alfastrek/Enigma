import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import zipfile
from cryptography.fernet import Fernet


# Functions for compression, encryption, decryption, and decompression
def compress_file(file_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, os.path.basename(file_path))

def encrypt_file(key, file_path, output_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, file_path, output_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")
        return False

def decompress_file(zip_path, output_folder):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(output_folder)

# Tkinter Interface
def browse_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        entry_csv_file_path.delete(0, tk.END)
        entry_csv_file_path.insert(0, file_path)

def browse_encrypted_zip_file():
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted ZIP Files", "*.zip")])
    if file_path:
        entry_encrypted_zip_file_path.delete(0, tk.END)
        entry_encrypted_zip_file_path.insert(0, file_path)

def browse_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_output_folder.delete(0, tk.END)
        entry_output_folder.insert(0, folder_path)

def compress_and_encrypt():
    file_path = entry_csv_file_path.get()
    output_folder = entry_output_folder.get()

    if not file_path:
        messagebox.showerror("Error", "Please select a CSV file first")
        return
    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder first")
        return
    
    # Step 1: Compress CSV into a ZIP file
    compressed_file = os.path.join(output_folder, os.path.basename(file_path) + ".zip")
    compress_file(file_path, compressed_file)

    # Step 2: Encrypt the compressed ZIP file
    encrypted_file = os.path.join(output_folder, os.path.basename(file_path) + "_encrypted.zip")
    key = Fernet.generate_key()  # Generate a random key
    encrypt_file(key, compressed_file, encrypted_file)
    
    # Display key in Text widget and copy to clipboard
    text_key.delete(1.0, tk.END)
    key_hex = key.decode('utf-8')  # Convert bytes to string for display
    text_key.insert(tk.END, key_hex)
    root.clipboard_clear()
    root.clipboard_append(key_hex)
    
    messagebox.showinfo("Success", f"CSV file compressed and encrypted successfully!\nEncrypted file saved at: {encrypted_file}")

def decrypt_and_decompress():
    file_path = entry_encrypted_zip_file_path.get()
    output_folder = entry_output_folder.get()
    
    if not file_path:
        messagebox.showerror("Error", "Please select an encrypted ZIP file first")
        return
    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder first")
        return

    key = entry_key.get().encode('utf-8')  # Get the key from entry
    if not key:
        messagebox.showerror("Error", "Please enter the decryption key")
        return

    # Step 1: Decrypt the encrypted ZIP file
    decrypted_file = os.path.join(output_folder, os.path.basename(file_path).replace("_encrypted", "_decrypted"))
    success = decrypt_file(key, file_path, decrypted_file)
    if not success:
        return
    
    # Step 2: Decompress the decrypted ZIP file
    decompress_file(decrypted_file, output_folder)
    
    
    messagebox.showinfo("Success", f"File decrypted and decompressed successfully!\nDecompressed files saved at: {output_folder}")

# Main window
root = tk.Tk()
root.title("CSV Compression & Encryption System")
root.geometry("600x500")
root.configure(bg="#181818")  # Dark background

# Create a style for the ttk elements
style = ttk.Style()
style.theme_use('clam')  # Use 'clam' for a minimal look

# Custom styles for LabelFrame
style.configure("Custom.TLabelframe", background="#2b2b2b", bordercolor="#444444")
style.configure("Custom.TLabelframe.Label", background="#2b2b2b", foreground="#ffffff")

# Title Label
label_title = ttk.Label(root, text="Compression & Encryption System", font=("Arial", 16, "italic"), background="#181818", foreground="#ffffff")
label_title.grid(row=0, column=0, columnspan=3, pady=10)

# CSV file selection for compression and encryption
frame_csv = ttk.LabelFrame(root, text="Compress & Encrypt CSV", padding=(10, 10), style="Custom.TLabelframe")
frame_csv.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

label_csv_file_path = ttk.Label(frame_csv, text="Select File:", background="#2b2b2b", foreground="#ffffff")
label_csv_file_path.grid(row=0, column=0, padx=10, pady=10)
entry_csv_file_path = ttk.Entry(frame_csv, width=40)
entry_csv_file_path.grid(row=0, column=1, padx=10, pady=10)
button_browse_csv = ttk.Button(frame_csv, text="Browse", command=browse_csv_file)
button_browse_csv.grid(row=0, column=2, padx=10, pady=10)

# Output folder selection
label_output_folder = ttk.Label(frame_csv, text="Select Output Folder:", background="#2b2b2b", foreground="#ffffff")
label_output_folder.grid(row=1, column=0, padx=10, pady=10)
entry_output_folder = ttk.Entry(frame_csv, width=40)
entry_output_folder.grid(row=1, column=1, padx=10, pady=10)
button_browse_output = ttk.Button(frame_csv, text="Browse", command=browse_output_folder)
button_browse_output.grid(row=1, column=2, padx=10, pady=10)

# Key display (for copying the generated key)
label_display_key = ttk.Label(frame_csv, text="Generated Key:", background="#2b2b2b", foreground="#ffffff")
label_display_key.grid(row=2, column=0, padx=10, pady=10)
text_key = scrolledtext.ScrolledText(frame_csv, height=2, width=40, wrap=tk.WORD, bg="#2b2b2b", fg="#ffffff", insertbackground='white')
text_key.grid(row=2, column=1, padx=10, pady=10)

# Compress and Encrypt Button
button_compress_encrypt = ttk.Button(frame_csv, text="Compress & Encrypt CSV", command=compress_and_encrypt)
button_compress_encrypt.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Encrypted ZIP file selection for decryption and decompression
frame_decrypt = ttk.LabelFrame(root, text="Decrypt & Decompress ZIP", padding=(10, 10), style="Custom.TLabelframe")
frame_decrypt.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

label_encrypted_zip_file_path = ttk.Label(frame_decrypt, text="Select Encrypted ZIP File:", background="#2b2b2b", foreground="#ffffff")
label_encrypted_zip_file_path.grid(row=0, column=0, padx=10, pady=10)
entry_encrypted_zip_file_path = ttk.Entry(frame_decrypt, width=40)
entry_encrypted_zip_file_path.grid(row=0, column=1, padx=10, pady=10)
button_browse_encrypted_zip = ttk.Button(frame_decrypt, text="Browse", command=browse_encrypted_zip_file)
button_browse_encrypted_zip.grid(row=0, column=2, padx=10, pady=10)

# Key input for decryption
label_key = ttk.Label(frame_decrypt, text="Enter Decryption Key (Base64):", background="#2b2b2b", foreground="#ffffff")
label_key.grid(row=1, column=0, padx=10, pady=10)
entry_key = ttk.Entry(frame_decrypt, width=40)
entry_key.grid(row=1, column=1, padx=10, pady=10)

# Decrypt and Decompress Button
button_decrypt_decompress = ttk.Button(frame_decrypt, text="Decrypt & Decompress ZIP", command=decrypt_and_decompress)
button_decrypt_decompress.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Main loop
root.mainloop()
