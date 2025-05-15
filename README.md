A Python script to send bulk WhatsApp messages using OCR to avoid resending. It automates browser interactions via PyAutoGUI, reads screenshots with Tesseract OCR,
and detects if a message has already been sent to a contact based on keywords. Useful for small businesses or campaigns needing message deduplication.
# WhatsApp Bulk Message Sender with OCR Check

This Python script sends WhatsApp messages in bulk via [web.whatsapp.com](https://web.whatsapp.com) while checking for duplicates using OCR (Optical Character Recognition). It detects if a message has already been sent to a contact based on screen text using `pytesseract`.

## ⚙️ Features
- Automatically sends text and location to a list of phone numbers
- Captures a screenshot of the chat window and uses OCR to detect previously sent messages
- Skips numbers where the message was already sent

## 🧰 Requirements

Install the following Python packages:

```bash
pip install pyautogui keyboard pillow pytesseract opencv-python pygetwindow
Also install Tesseract OCR and add it to your system PATH.

Example Tesseract install path:

makefile
Copy
Edit
C:\Program Files\Tesseract-OCR\tesseract.exe
🗂 Folder Structure
php
Copy
Edit
sms/
├── final.py               # Main script
├── num.txt                # List of phone numbers (one per line, without +91)
└── trash/
    └── check.png          # Temporary screenshot used for OCR
📄 Setup Instructions
Prepare a num.txt file with one phone number per line (without country code).

Update the absolute path to check.png in the script if needed.

Launch https://web.whatsapp.com and scan the QR code.

Run the script:

bash
Copy
Edit
python final.py
⚠️ Notes
Coordinate clicks (like pg.click(540,164)) are screen-resolution dependent. Adjust them using a mouse coordinate tool if needed.

Make sure WhatsApp Web stays focused while the script runs.

The messages and keywords for OCR can be changed directly in the script.

🧠 How It Works
Opens WhatsApp Web.

For each number in num.txt:

Searches the contact.

Takes a screenshot of the chat window.

Crops and preprocesses it for OCR.

If keywords are found in the text, skip sending.

Otherwise, paste the messages and send them.

Author: Shobhit
