import shutil
import tkinter as tk
from tkinter import filedialog

def upload_file():
    # Get the local file location
    local_file = filedialog.askopenfilename(
        title="Select the local file",
        filetypes=(("PDF Files", "*.pdf"), ("CSV Files", "*.csv"), ("XML Files", "*.xml"), ("EDI Files", "*.edi"), ("All Files", "*.*"))
    )

    # Get the Windows Server file location
    server_file = filedialog.asksaveasfilename(
        title="Save the file to the Windows Server",
        defaultextension=".pdf",
        filetypes=(("PDF Files", "*.pdf"), ("CSV Files", "*.csv"), ("XML Files", "*.xml"), ("EDI Files", "*.edi"), ("All Files", "*.*"))
    )

    # Copy the local file to the Windows Server file location
    shutil.copy(local_file, server_file)

# Create the GUI
root = tk.Tk()
root.title("Upload File to Windows Server")

# Create the "Upload" button
upload_button = tk.Button(root, text="Upload", command=upload_file)
upload_button.pack()

# Run the GUI
root.mainloop()
