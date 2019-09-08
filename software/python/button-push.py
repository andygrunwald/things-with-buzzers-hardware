#
# Small script to test the functionality of the hardware buzzers. 
#
# We use the well-known RPi.GPIO library for the use case.
# Check out more about the library here: https://pypi.org/project/RPi.GPIO/
#
import os
import RPi.GPIO as GPIO
import time
import subprocess

# Define Raspberry PI GPIO pins for all four buttons.
# These pins are for the button itself.
PIN_BTN_RED = 21
PIN_BTN_GREEN = 20
PIN_BTN_BLUE = 16
PIN_BTN_YELLOW = 12

# These pins are for the LEDs inside the button.
PIN_LED_RED = 26
PIN_LED_GREEN = 19
PIN_LED_BLUE = 13
PIN_LED_YELLOW = 6

# Set the right GPIO pin layout.
# See "What is the difference between BOARD and BCM for GPIO pin numbering?"
# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setmode(GPIO.BCM)

# Set input signals for the buttons.
GPIO.setup(PIN_BTN_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BTN_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BTN_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BTN_YELLOW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set output signals for the LEDs.
GPIO.setup(PIN_LED_RED, GPIO.OUT)
GPIO.output(PIN_LED_RED, GPIO.LOW)
GPIO.setup(PIN_LED_GREEN, GPIO.OUT)
GPIO.output(PIN_LED_GREEN, GPIO.LOW)
GPIO.setup(PIN_LED_BLUE, GPIO.OUT)
GPIO.output(PIN_LED_BLUE, GPIO.LOW)
GPIO.setup(PIN_LED_YELLOW, GPIO.OUT)
GPIO.output(PIN_LED_YELLOW, GPIO.LOW)

# Store the status of the LEDs.
# Default, all leds are off.
leds = {
    PIN_LED_RED: False,
    PIN_LED_GREEN: False,
    PIN_LED_BLUE: False,
    PIN_LED_YELLOW: False
}
def buttonDown(channel):
    """
    Print which button was hit and trigger the related LED.
    If the LED is off (default), switch it on when the button is hit.
    If the LED is on (e.g., after the first button hit), switch it off.

    `channel` is the GPIO pin number of the hit button.
    """
    global leds 

    # Print which button color was hit.
    buttons = {
        PIN_BTN_RED: "Red \033[41m  \033[0m",
        PIN_BTN_GREEN: "Green \033[42m  \033[0m",
        PIN_BTN_BLUE: "Blue \033[44m  \033[0m",
        PIN_BTN_YELLOW: "Yellow \033[1;43m  \033[0m"
    }
    output = buttons.get(channel, "Unknown button colour")
    output += " button pushed"
    print(output)

    # Create a relation which button hit needs 
    # to activate which LED.
    button_led_mapping = {
        PIN_BTN_RED: PIN_LED_RED,
        PIN_BTN_GREEN: PIN_LED_GREEN,
        PIN_BTN_BLUE: PIN_LED_BLUE,
        PIN_BTN_YELLOW: PIN_LED_YELLOW
    }

    # Determine the right LED per button.
    led = button_led_mapping.get(channel, "Unknown button")
    led_status = leds.get(led, "Unknown button led")
    if (led_status == True):
        leds[led] = False
        GPIO.output(led, GPIO.LOW)
    else:
        leds[led] = True
        GPIO.output(led, GPIO.HIGH)

# Add event listener to detect input signals from the buttons.
# In case of button hit, execute the callback.
GPIO.add_event_detect(PIN_BTN_RED, GPIO.RISING, callback=buttonDown, bouncetime=300)
GPIO.add_event_detect(PIN_BTN_GREEN, GPIO.RISING, callback=buttonDown, bouncetime=300)
GPIO.add_event_detect(PIN_BTN_BLUE, GPIO.RISING, callback=buttonDown, bouncetime=300)
GPIO.add_event_detect(PIN_BTN_YELLOW, GPIO.RISING, callback=buttonDown, bouncetime=300)

# Start the main loop keep it running.
print("Button push script started: Go crazy and push a buzzer!")
try:
    while True:
        time.sleep(1)
finally:
    GPIO.cleanup()