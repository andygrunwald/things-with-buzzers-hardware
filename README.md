# Things with buzzers: Hardware

Build your own hardware game show buzzers and do [awesome things](#things-you-can-do-with-buzzers) with it! 🚀

This repository contains everything you need to build hardware buzzers and connecting them with your software.
Start today having fun, and make people happy by providing them an unforgettable time.

<p align="center">
  <img src="images/buzzers-raspberrypi.jpg" title="The finished product: Four buzzers, a Raspberry Pi incl. hat" alt="The finished product: Four buzzers, a Raspberry Pi incl. hat">
</p>

## How we build and run them

We built four game show buzzers in four different colors (red, green, blue, yellow).
The buzzer cases are self-printed with a 3D-Printer.
Each buzzer case has a female USB connector embedded.

The central control unit is a Raspberry Pi 3 Model B+ (following _Pi_) with a custom build hat module (circuit board).
The hat module offers four female USB connectors and maps them onto the GPIO of the Pi.

Each buzzer connects via a USB cable to the Pi hat.
On the Pi, we can place software and read the buzzer signals (e.g., buzzer pressed) and react on this.

If the software (running on the Pi) offers a UI and the Pi connects to a network (or opens up a new network), a client can connect to it.
As a small software example: Show in the UI which button is pressed.

It is how it looks like:

<p align="center">
  <img src="images/buzzer-setup.png" title="The complete setup: Buzzer -> USB -> Raspberry Pi -> Computer" alt="The complete setup: Buzzer -> USB -> Raspberry Pi -> Computer">
</p>

## What we need / Bill of material (BOM)

## Buzzers

## Raspberry Pi Hat

## Raspberry Pi

## How we can test the buzzers (with software)

## Things you can do with buzzers

* Running a Jeopardy! game show
* Stopping athletes time during a sports event

## Credits

A big thank you to [Lars Heß / @lhess](https://github.com/lhess) and [Matthias Endler / @mre](https://github.com/mre).
Without them, this project would not happen.

Lars has designed and built the complete hardware.
Matthias helped a lot with the software and motivation part 😀