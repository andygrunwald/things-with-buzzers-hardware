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

## What we need / Bill of materials (BOM)

To replicate this project and build your buzzers, you need a couple of things.
We have created a complete list of what you need, a so-called _Bill of material (BOM)_.

Check it out: [Bill of materials (BOM)](./bill-of-materials.md).

## Buzzers

First, we start with the buzzer case and print it with a 3D printer.
Printing instructions / Step files can be found in the [3d-models folder](./3d-models).
Feel free to choose the color of your printing material for the right look.
Go ahead and print!

If you are new to 3D printing, step files are printing instructions.
You can few and edit them with software like [Fusion 360 from Autodesk](https://www.autodesk.com/products/fusion-360/free-trial) (they offer [a free version for startups and hobbyists](https://www.autodesk.com/campaigns/fusion-360-for-hobbyists)).

<p align="center">
  <img width="400" src="images/3d-buzzer-housing.png" title="3D model of the buzzer case" alt="3D model of the buzzer case">
  <img width="400" src="images/3d-buzzer-lid.png" title="3D model of the buzzer lid" alt="3D model of the buzzer lid">
</p>

Next step would be to build the small circuit board that connects the buzzer with the USB socket.
For this, we created a step-by-step image guide.
Check it out in our [buzzer building folder](./images/buzzer-building/README.md).

Congratulations, you build your first game show buzzer. How awesome is this?

## Raspberry Pi Hat

## Raspberry Pi

On the Raspberry Pi (following _Pi_) itself, we install a [standard Raspbian Lite operating system](https://www.raspberrypi.org/downloads/raspbian/) without any desktop functionality.

To access the Pi from an external client (e.g., laptop or mobile phone) you should connect it to a network.
Either to an existing one via a typical RJ45 LAN cable or a wireless network (can be done via [`raspi-config`](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)).
If you want to run it completely independent and maybe offline, we recommend to [configure the Pi as a wireless access point](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md).

Add the Pi hat onto the GPIO and move on to your first software tests.

## How we can test the buzzers (with software)

## Things you can do with buzzers

* Running a Jeopardy! game show
* Stopping athletes time during a sports event

## Credits

A big thank you to [Lars Heß / @lhess](https://github.com/lhess) and [Matthias Endler / @mre](https://github.com/mre).
Without them, this project would not happen.

Lars has designed and built the complete hardware.
Matthias helped a lot with the software and motivation part 😀