import pyfirmata
import time
from pyfirmata import util
from sklearn.metrics import PredictionErrorDisplay

# Connect to the Arduino board
board = pyfirmata.Arduino('COM12') # replace 'COM6' with your Arduino's port

# Define the LCD display
lcd = board.get_pin('a:0:i') # replace 'a:0:i' with the I2C address of your LCD

# Function to print messages on the LCD
def print_lcd(text):
   if text:
       board.send_sysex(util.STRING_DATA, util.str_to_two_byte_iter(text))

# ... your existing code ...

predicted_sign = labels_dict[int(PredictionErrorDisplay[0])]
print_lcd(predicted_sign) # print the message on the LCD

# ... your existing code ...
