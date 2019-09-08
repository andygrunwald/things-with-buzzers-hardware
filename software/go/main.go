/**
 * Small app to test the functionality of the hardware buzzers.
 *
 * Whatever you do with the GPIO pins the raw BCM2835 pinout mapping to Raspberry Pi at
 * https://godoc.org/github.com/stianeikeland/go-rpio is super helpful.
 *
 */
package main

import (
	"fmt"
	"os"
	"sync"
	"time"

	"github.com/stianeikeland/go-rpio"
)

func main() {
	// Define Raspberry PI GPIO pins for all four buttons.
	// These pins are for the button itself.
	//
	// @TODO This app does not support the LEDs in the buttons
	// If you read this, feel free to add LED support
	redButton := rpio.Pin(21)
	greenButton := rpio.Pin(20)
	blueButton := rpio.Pin(16)
	yellowButton := rpio.Pin(12)

	// Open and map memory to access gpio
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer rpio.Close()

	// Set input signals for the buttons.
	redButton.Input()
	redButton.PullUp()
	redButton.Detect(rpio.FallEdge)     // enable falling edge event detection
	defer redButton.Detect(rpio.NoEdge) // disable edge event detection

	greenButton.Input()
	greenButton.PullUp()
	greenButton.Detect(rpio.FallEdge)
	defer greenButton.Detect(rpio.NoEdge)

	blueButton.Input()
	blueButton.PullUp()
	blueButton.Detect(rpio.FallEdge)
	defer blueButton.Detect(rpio.NoEdge)

	yellowButton.Input()
	yellowButton.PullUp()
	yellowButton.Detect(rpio.FallEdge)
	defer yellowButton.Detect(rpio.NoEdge)

	// Define the listener function for buzzer hits
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		for {
			// Check if an event occured
			if redButton.EdgeDetected() {
				fmt.Println("Red \033[41m  \033[0m button pushed")
			}

			if greenButton.EdgeDetected() {
				fmt.Println("Green \033[42m  \033[0m button pushed")
			}

			if blueButton.EdgeDetected() {
				fmt.Println("Blue \033[44m  \033[0m button pushed")
			}

			if yellowButton.EdgeDetected() {
				fmt.Println("Yellow \033[1;43m  \033[0m button pushed")
			}
			time.Sleep(time.Second / 2)
		}
	}()

	// Let's go
	fmt.Println("Button push app started: Go crazy and push a buzzer!")
	wg.Wait()
}
