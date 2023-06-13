import time
import keyboard
import clipboard

print("Press Ctrl+Shift+T key to type the last copied text.\nPress ESC to stop the program")

while True:
    # Check if CTRL+SHIFT+T key is pressed
    if keyboard.is_pressed("CTRL") and keyboard.is_pressed("SHIFT") and keyboard.is_pressed("T"):
        # Get the text from the clipboard
        text = clipboard.paste()
        # Write the text using the keyboard
        keyboard.write(text)

    # Check if the ESC key is pressed
    if keyboard.is_pressed("esc"):
        # Break the loop if the ESC key is pressed
        break

    # Wait 0.1 seconds before continuing
    time.sleep(0.1)