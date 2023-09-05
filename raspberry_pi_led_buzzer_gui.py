import RPi.GPIO as GPIO
import tkinter as tk

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 11 as an output for the LED
GPIO.setup(17, GPIO.OUT)

# Set pin 12 as an output for the buzzer
GPIO.setup(18, GPIO.OUT)

# Create the GUI window
root = tk.Tk()
root.title("LED and Buzzer Control")

# Function to turn the LED on
def turn_on_led():
    GPIO.output(17, GPIO.HIGH)

# Function to turn the LED off
def turn_off_led():
    GPIO.output(17, GPIO.LOW)

# Function to turn the buzzer on
def turn_on_buzzer():
    GPIO.output(18, GPIO.HIGH)

# Function to turn the buzzer off
def turn_off_buzzer():
    GPIO.output(18, GPIO.LOW)

# Create buttons in the GUI
btn_led_on = tk.Button(root, text="LED On", command=turn_on_led)
btn_led_on.pack()

btn_led_off = tk.Button(root, text="LED Off", command=turn_off_led)
btn_led_off.pack()

btn_buzzer_on = tk.Button(root, text="Buzzer On", command=turn_on_buzzer)
btn_buzzer_on.pack()

btn_buzzer_off = tk.Button(root, text="Buzzer Off", command=turn_off_buzzer)
btn_buzzer_off.pack()

# Start the GUI main loop
root.mainloop()

# Cleanup GPIO on exit
GPIO.cleanup()
